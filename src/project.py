from typing import Optional
from sqlmodel import Field, SQLModel

from src.config import Config

class Projects(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project: str
    message_stack_json: str