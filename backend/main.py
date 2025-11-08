from fastapi import FastAPI
from contextlib import asynccontextmanager

from db import init_db


app = FastAPI(
    title="Agent-Recon",
    version="0.1.0"
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Starting Up")
    init_db()
    print("DB Initialized")





app.get("/")
def read_root():
    return {"status":"working", "msg":"server running"}









