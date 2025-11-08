
from datetime import datetime, UTC
from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
  
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    name: Optional[str] = Field(default=None)
    passwordHash: str 
    
    role: str = Field(default="investigator") #'investigator', 'admin'
    created_at: datetime.datetime = Field(default_factory=lambda: datetime.now(UTC))