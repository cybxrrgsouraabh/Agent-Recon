
import json
import datetime
from sqlmodel import Session
from models.audit import AuditLog
from datetime import UTC, datettime


def record_action(
    db: Session,
    user: str,
    action: str,
    payload_obj: dict,
    resource_type: str = None,
    resource_id: int = None
) -> AuditLog:
    """
    Records a new action in the simple audit log.
    """
    
    # 4. Create the new log entry object
    new_log_entry = AuditLog(
        user=user,
        action=action,
        resource_type=resource_type,
        resource_id=resource_id,
        timestamp=datetime.now(UTC),
        payload=payload_obj 
    )
    
    # 5. Save to the database
    db.add(new_log_entry)
    db.commit() 
    db.refresh(new_log_entry)
    
    return new_log_entry