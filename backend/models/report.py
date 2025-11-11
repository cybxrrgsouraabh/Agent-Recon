
from datetime import UTC, datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class Report(SQLModel, table=True):
    # """ Represents a generated report, including its signature for verification. """

    __tablename__ = "reports"

    id: Optional[int] = Field(default=None, primary_key=True)
    case_id: Optional[str] = Field(default=None, index=True)
    
    generated_by: Optional[str] = Field(default=None, foreign_key="user.id") 
    generated_at: datetime = Field(default_factory=lambda:datetime.now(UTC))
    
    file_path: str = Field(unique=True)
    file_sha256: str = Field(max_length=64)
    
    signature: str = Field(description="Digital signature of the file_sha256")
    notes: Optional[str] = Field(default=None)

    