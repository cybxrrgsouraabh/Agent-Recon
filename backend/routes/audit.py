from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from db import get_session
from models.audit import AuditLog





router = APIRouter()

@router.get("/")
def welcome():
    return {"msg": "welcome to aufit log"}


@router.get("/log", response_model=list[AuditLog])
async def get_audit_log(db: Session = Depends(get_session)):
    query = select(AuditLog).order_by(AuditLog.id)
    logs = db.exec(query).all()
    print(logs)
    return logs


