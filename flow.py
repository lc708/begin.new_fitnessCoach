from macore import Flow
from nodes import (
    DataValidationNode, 
    GoalAnalysisNode, 
    PlanGenerationNode, 
    PlanOptimizationNode
)

def create_fitness_plan_flow():
    """创建健身计划生成流程"""
    # 创建节点实例
    data_validation = DataValidationNode()
    goal_analysis = GoalAnalysisNode()
    plan_generation = PlanGenerationNode()
    plan_optimization = PlanOptimizationNode()
    
    # 连接节点 - 使用动作标签连接
    data_validation - "goal_analysis" >> goal_analysis
    goal_analysis - "plan_generation" >> plan_generation
    plan_generation - "plan_optimization" >> plan_optimization
    
    # 创建以数据验证节点开始的流程
    return Flow(start=data_validation)

# 创建健身计划生成流程实例
fitness_flow = create_fitness_plan_flow()