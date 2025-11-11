

from datetime import datetime, UTC
from typing import Optional, Any
from sqlmodel import Field, SQLModel, Relationship, JSON, Column

class Event(SQLModel, table=True):

    # Represents a single parsed event from a piece of evidence.
    # This model has a many-to-one relationship with Evidence.
  
    __tablename__ = "events"

    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Relationship: Belongs to one Evidence
    evidence_id: Optional[int] = Field(default=None, foreign_key="evidence.id", index=True)
    
    # We use a string "Evidence" to tell SQLModel the type
    evidence_source: Optional["Evidence"] = Relationship(back_populates="events")

    # Provenance (Where did this come from?)
    line_number: Optional[int] = Field(default=None)
    raw_text: Optional[str] = Field(default=None)
    
    # Parsing Details (How was this extracted?)
    extraction_rule: Optional[str] = Field(default=None) # RULEBASED | AI (PARSERS)
    extraction_confidence: Any = Field(default=None, sa_column=Column(JSON))
    
    # Timestamp Details (When did this happen?)
    parsed_timestamp_original: Optional[str] = Field(default=None)
    timestamp_utc: Optional[datetime] = Field(default=None, index=True)
    
    # Parsed Content
    device: Optional[str] = Field(default=None, index=True)
    event_type: Optional[str] = Field(default=None, index=True)

    