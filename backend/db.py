
import os
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv

load_dotenv()



DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Database URL: {DATABASE_URL}")



engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

def init_db():
    
    # Initializes the database and creates all tables.
    # Import all models here so SQLModel knows about them
    from models.user import User
    from models.evidence import Evidence
    from models.event import Event
    from models.audit import AuditLog
    from models.report import Report
    from models.parsemapping import ParseMapping 

    SQLModel.metadata.create_all(engine)
    print("database tables created")

def get_session():
    
    with Session(engine) as session:
        yield session