# models/audit.py

from datetime import UTC, datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class AuditLog(SQLModel, table=True):
    # """ An immutable, chained log of all actions taken in the system. """

    __tablename__ = "audit_log"

    id: Optional[int] = Field(default=None, primary_key=True)
    
    user: Optional[str] = Field(default=None, foreign_key="user.id") # Or ForeignKey("user.id")
    action: str = Field(index=True) # e.g., UPLOAD, PARSE, DELETE
    
    resource_type: Optional[str] = Field(default=None) # e.g., 'evidence', 'report'
    resource_id: Optional[int] = Field(default=None)
    
    timestamp: datetime = Field(default_factory=lambda:datetime.now(UTC), index=True)
    
    # --- Chain of Custody ---
    payload: str = Field(description="Canonical JSON string of action details")



    