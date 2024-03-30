
from typing import Optional
from sqlmodel import Field, SQLModel


class AgentStateModel(SQLModel, table=True):
    __tablename__ = "agent_state"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    project: str
    state_stack_json: str