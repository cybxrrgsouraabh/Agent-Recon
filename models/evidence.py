
from datetime import datetime, UTC
from typing import Optional, List, Any
from sqlmodel import Field, SQLModel, Relationship, JSON, Column

class Evidence(SQLModel, table=True):
  
    # This model has a one-to-many relationship with Event.

    __tablename__ = "evidence"

    id: Optional[int] = Field(default=None, primary_key=True)
    case_id: Optional[str] = Field(default=None, index=True)
    
    original_filename: Optional[str] = Field(default=None)
    stored_path: str = Field(unique=True)
    sha256: str = Field(max_length=64, unique=True)
    size_bytes: Optional[int] = Field(default=None)
    
    uploaded_by: Optional[str] = Field(deafult="None", foreign_key="user.id") 
    uploaded_at: datetime.datetime = Field(default_factory=lambda : datetime.now(UTC))
    
    status: str = Field(default="UPLOADED") # UPLOADED|PARSING|PARSED|ERROR
    notes: Any = Field(default=None, sa_column=Column(JSON))

    # Relationship: One Evidence has many Events
    # We use a string "Event" to tell SQLModel the type
    events: List["Event"] = Relationship(back_populates="evidence_source")
    parsemapping: List["ParseMapping"] = Relationship(back_populates="evidence")