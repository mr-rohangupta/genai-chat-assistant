from pydantic import BaseModel, Field

class AgentState(BaseModel):
    # Original User Question
    question: str

    # Planner output
    plan: str | None = None

    # Current execution step
    current_step: str | None = None

    # Completed steps
    completed_steps: list = Field(
        default_factory=list
    )

    thought: str | None = None

    action: str | None = None

    observation: list = Field(
        default_factory=list
    )

    reflection: str | None = None

    answer: str | None = None

    retry_count: int = 0