
from datetime import UTC, datetime
from typing import List, Optional, Any
from sqlmodel import Field, Relationship, SQLModel, JSON, Column

class ParseMapping(SQLModel, table=True):

    # Stores a learned or manually defined parsing rule.
    # e.g., for a specific device_type or file_hash.
    
    __tablename__ = "parsemapping"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Many to 1 relationship with evidence
    evidence_id: Optional[int] = Field(default=None, foreign_key="user.id")
    evidence_source: List["Evidence"] = Relationship(back_populates="parsemapping")

    # A way to identify this rule
    rule_name: str = Field(unique=True)
    device_type: Optional[str] = Field(default=None, index=True)
    
    # The actual parsing rules, stored as JSON
    # e.g., {"timestamp_regex": "...", "fields": [...]}
    mapping_rules: Any = Field(default=None, sa_column=Column(JSON))
    
    parser_type: str = Field(default="AI-BASED") # 'AI-BASED', 'RULE-BASED'
    
    created_at: datetime = Field(default_factory=lambda:datetime.now(UTC))
    created_by: Optional[str] = Field(default=None)