from dotenv import load_dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import init_db

# importing my routes here 
from routes import audit as audit_router


load_dotenv()

app = FastAPI(
    title="Agent-Recon",
    version="0.1.0"
)


@app.get("/")
def testing():
    return {"msg":"working server"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Starting Up")
    init_db()
    print("DB Initialized")

app.include_router(
    audit_router.router,
    prefix="/audit",
    tags=["Audit (list)"]
)









