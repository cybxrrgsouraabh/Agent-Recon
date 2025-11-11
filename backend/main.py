from fastapi import FastAPI
from contextlib import asynccontextmanager

from db import init_db




@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Starting Up")
    init_db()
    print("DB Initialized")
    yield
    print("APPLICATION CLOSING")

app = FastAPI(
    title="Agent-Recon",
    version="0.1.0",
    lifespan=lifespan
)
@app.get("/")
def read_root():
    return {"status":"working", "msg":"server running"}









