"""
FastAPI后端 - 提供健身计划生成API
"""
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
import logging
import sys
import os

# 加载.env文件
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # 在生产环境中可能不需要dotenv

# 强制使用更快的LLM - 通过OPENROUTER使用GEMINI 2.5 FLASH
os.environ["LLM_PROVIDER"] = "openrouter"

# 添加父目录到路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flow import create_fitness_plan_flow
from datetime import datetime

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建FastAPI应用
app = FastAPI(
    title="FitCoach API",
    description="个性化健身训练计划生成API",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该限制为特定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型定义
class BasicInfo(BaseModel):
    age: int = Field(..., ge=16, le=80, description="年龄，16-80岁")
    gender: str = Field(..., pattern="^(男|女)$", description="性别")
    height: float = Field(..., ge=140, le=220, description="身高，140-220cm")
    weight: float = Field(..., ge=40, le=200, description="体重，40-200kg")
    experience: str = Field(..., pattern="^(beginner|intermediate|advanced)$", description="健身经验")

class Goals(BaseModel):
    primary_goal: str = Field(..., pattern="^(weight_loss|muscle_gain|strength|endurance|toning)$", description="主要目标")
    target_areas: Optional[List[str]] = Field(default=["全身"], description="目标训练部位")
    timeline: Optional[str] = Field(default="4周", description="目标时间线")

class Schedule(BaseModel):
    days_per_week: int = Field(..., ge=2, le=6, description="每周训练天数")
    time_per_session: int = Field(..., ge=20, le=120, description="每次训练时长（分钟）")

class Limitations(BaseModel):
    injuries: Optional[List[str]] = Field(default=[], description="伤病史")
    restrictions: Optional[List[str]] = Field(default=[], description="身体限制")

class UserDataRequest(BaseModel):
    basic_info: BasicInfo
    goals: Goals
    schedule: Schedule
    limitations: Optional[Limitations] = Field(default_factory=Limitations)

class PlanResponse(BaseModel):
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    timestamp: str
    generation_time: Optional[float] = None

# API端点

@app.get("/")
async def root():
    """根路径"""
    return {
        "message": "FitCoach API - 个性化健身训练计划生成服务",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/api/health")
async def health_check():
    """健康检查端点"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "FitCoach API"
    }

@app.post("/api/generate-plan", response_model=PlanResponse)
async def generate_plan(user_data: UserDataRequest):
    """
    生成个性化训练计划
    
    Args:
        user_data: 用户输入数据
        
    Returns:
        PlanResponse: 包含生成的训练计划或错误信息
    """
    start_time = datetime.now()
    
    try:
        logger.info("收到训练计划生成请求")
        
        # 调试：打印收到的原始数据
        logger.info(f"用户提交的基本信息: {user_data.basic_info}")
        logger.info(f"用户提交的目标: {user_data.goals}")
        logger.info(f"用户提交的时间安排: {user_data.schedule}")
        logger.info(f"用户提交的限制: {user_data.limitations}")
        
        # 转换Pydantic模型为字典
        user_data_dict = {
            "basic_info": user_data.basic_info.model_dump(),
            "goals": user_data.goals.model_dump(),
            "schedule": user_data.schedule.model_dump(),
            "limitations": user_data.limitations.model_dump() if user_data.limitations else {"injuries": [], "restrictions": []}
        }
        
        # 初始化共享存储
        shared = {
            "user_data": user_data_dict,
            "validation_errors": [],
            "data_is_valid": False,
            "analysis_result": {},
            "raw_plan": {},
            "final_plan": {},
            "generation_completed": False
        }
        
        # 创建并运行健身计划生成流程
        logger.info("开始生成训练计划")
        fitness_flow = create_fitness_plan_flow()
        fitness_flow.run(shared)
        
        # 检查生成结果
        if shared.get('generation_completed', False):
            logger.info("训练计划生成成功")
            
            generation_time = (datetime.now() - start_time).total_seconds()
            
            return PlanResponse(
                success=True,
                data={
                    "plan": shared['final_plan']['formatted_plan'],
                    "generation_info": {
                        "optimization_success": shared['final_plan'].get('optimization_success', True),
                        "validation_errors": shared.get('validation_errors', [])
                    }
                },
                error=None,
                timestamp=datetime.now().isoformat(),
                generation_time=generation_time
            )
        else:
            logger.warning("训练计划生成失败")
            
            return PlanResponse(
                success=False,
                data=None,
                error="训练计划生成失败，请检查输入数据",
                timestamp=datetime.now().isoformat()
            )
            
    except Exception as e:
        logger.error(f"API错误: {e}")
        
        return PlanResponse(
            success=False,
            data=None,
            error=f"服务器内部错误: {str(e)}",
            timestamp=datetime.now().isoformat()
        )

@app.get("/api/goal-options")
async def get_goal_options():
    """获取可选的健身目标"""
    return {
        "goals": [
            {"value": "weight_loss", "label": "减脂塑形", "description": "减少体脂，塑造身形"},
            {"value": "muscle_gain", "label": "增肌塑体", "description": "增加肌肉量，提升力量"},
            {"value": "strength", "label": "力量提升", "description": "提高最大力量和爆发力"},
            {"value": "endurance", "label": "耐力增强", "description": "提升心肺功能和持久力"},
            {"value": "toning", "label": "身体塑形", "description": "塑造身体线条，维持健康"}
        ],
        "experience_levels": [
            {"value": "beginner", "label": "初学者", "description": "0-6个月健身经验"},
            {"value": "intermediate", "label": "有经验", "description": "6个月-2年健身经验"},
            {"value": "advanced", "label": "高级", "description": "2年以上健身经验"}
        ],
        "target_areas": [
            "全身", "胸部", "背部", "腿部", "肩部", "手臂", "核心", "有氧"
        ]
    }

@app.get("/api/exercise-preview")
async def get_exercise_preview():
    """获取训练动作预览"""
    from utils.fitness_knowledge import get_exercise_database
    
    try:
        exercises = get_exercise_database()
        
        # 简化输出，每个部位只返回前3个动作
        preview = {}
        for area, levels in exercises.items():
            preview[area] = []
            for level, exercise_list in levels.items():
                for exercise in exercise_list[:2]:  # 每个水平只取前2个
                    preview[area].append({
                        "name": exercise["name"],
                        "difficulty": exercise["difficulty"],
                        "equipment": exercise["equipment"],
                        "description": exercise["description"]
                    })
        
        return {"exercises": preview}
        
    except Exception as e:
        logger.error(f"获取动作预览失败: {e}")
        return {"error": "无法获取动作预览"}

if __name__ == "__main__":
    import uvicorn
    
    # 开发环境运行
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
