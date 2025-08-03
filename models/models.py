from typing import Optional
from sqlmodel import Field, SQLModel

#DB Schema
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True)
    role: str = Field(default="volunteer")

# New User Model Schema
class UserCreate(SQLModel):
    name: str
    email: str
    role: Optional[str] = "volunteer"
