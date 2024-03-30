from typing import Optional
from sqlmodel import Field, SQLModel


class Knowledge(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tag: str
    contents: str