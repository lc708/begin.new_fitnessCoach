# 🏋️ FitCoach - 个性化健身训练计划生成器

一个基于 AI 驱动的个性化健身训练计划生成应用，帮助用户获得科学合理的健身指导。

## ✨ 主要特性

- 🎯 **个性化定制**: 基于用户身体数据和健身目标智能匹配
- 🔬 **科学安全**: 专业的训练建议、动作指导和安全提醒  
- 🔒 **隐私保护**: 完全不保存任何用户个人信息
- 📱 **响应式设计**: 支持电脑和手机端使用
- ⚡ **即时生成**: AI快速生成详细训练计划
- 🎨 **用户友好**: 直观的界面和清晰的计划展示

## 🚀 技术栈

### 后端
- **框架**: FastAPI + MACore (智能工作流)
- **AI服务**: OpenAI GPT-5-mini / Google Gemini / DeepSeek
- **数据处理**: Pydantic 数据验证

### 前端  
- **框架**: React 18 + Vite
- **样式**: Tailwind CSS v3
- **路由**: React Router
- **状态管理**: Context API

### 部署
- **平台**: Vercel (全栈部署)
- **域名**: 支持自定义域名
- **分析**: Vercel Analytics

## 📦 快速开始

### 环境要求
- Python 3.8+
- Node.js 16+
- npm 或 yarn

### 1. 克隆项目
```bash
git clone <repository-url>
cd bpapp_005_fitcoach
```

### 2. 安装依赖
```bash
# 安装后端依赖
pip install -r requirements.txt

# 安装前端依赖
cd frontend
npm install
```

### 3. 配置环境变量
```bash
# 复制环境变量模板
cp .env.template .env
```

编辑 `.env` 文件，添加你的 API 密钥:
```env
OPENAI_API_KEY=your_openai_api_key_here
LLM_PROVIDER=openai
OPENAI_MODEL=gpt-5-mini
```

### 4. 运行应用

**启动后端服务:**
```bash
cd backend
python api.py
# 后端服务: http://localhost:8000
```

**启动前端服务:**
```bash
cd frontend  
npm run dev
# 前端应用: http://localhost:3000
```

### 5. 测试功能

**Web界面:**
访问 http://localhost:3000 体验完整的用户界面

**命令行测试:**
```bash
# 使用示例数据测试
python main.py

# 使用自定义数据测试
python main.py --custom
```

## 🌐 部署到 Vercel

### 自动部署
1. 推送代码到 GitHub
2. 在 [Vercel](https://vercel.com) 中导入项目
3. 配置环境变量:
   - `OPENAI_API_KEY`: 你的 OpenAI API 密钥
   - `LLM_PROVIDER`: `openai` (或其他支持的提供商)
   - `OPENAI_MODEL`: `gpt-5-mini`
4. 点击部署

### 手动部署
```bash
# 安装 Vercel CLI
npm i -g vercel

# 部署
vercel --prod
```

## 📁 项目结构

```
bpapp_005_fitcoach/
├── 📁 backend/              # FastAPI 后端
│   ├── api.py              # API 路由和逻辑
│   └── requirements.txt    # Python 依赖
├── 📁 frontend/            # React 前端
│   ├── src/
│   │   ├── pages/          # 页面组件
│   │   ├── components/     # 可复用组件
│   │   └── context/        # 状态管理
│   ├── package.json        # Node.js 依赖
│   └── tailwind.config.js  # Tailwind 配置
├── 📁 utils/               # 工具函数
│   ├── call_llm.py         # LLM 调用封装
│   ├── fitness_knowledge.py # 健身知识库
│   └── plan_formatter.py   # 计划格式化
├── 📁 docs/                # 项目文档
│   ├── design.md           # 设计文档
│   └── detail_note.md      # 开发记录
├── flow.py                 # MACore 流程定义
├── nodes.py                # MACore 节点实现  
├── main.py                 # 命令行入口
├── vercel.json             # Vercel 配置
└── README.md               # 项目说明
```

## 🔧 API 接口

### 主要端点

**生成训练计划**
```http
POST /api/generate-plan
Content-Type: application/json

{
  "basic_info": {
    "age": 25,
    "gender": "男", 
    "height": 175,
    "weight": 70,
    "experience": "beginner"
  },
  "goals": {
    "primary_goal": "muscle_gain",
    "target_areas": ["chest", "arms"]
  },
  "schedule": {
    "days_per_week": 3,
    "time_per_session": 45
  },
  "limitations": {
    "injuries": [],
    "restrictions": []
  }
}
```

**健康检查**
```http
GET /api/health
```

**获取选项**
```http
GET /api/goal-options
```

## 🎯 使用流程

1. **填写信息** - 输入基本身体数据和健身目标
2. **AI分析** - 系统智能分析用户需求和身体状况
3. **生成计划** - 生成个性化的详细训练计划
4. **保存使用** - 截图保存计划，开始健身之旅

## ⚠️ 重要提醒

- 本应用提供的训练计划仅供参考，不能替代专业健身指导
- 开始任何训练计划前建议咨询专业教练或医生
- 应用不保存任何用户个人信息，请截图保存您的训练计划
- 训练过程中如有不适请立即停止并寻求专业帮助

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

---

**安全训练，健康生活！🏆**