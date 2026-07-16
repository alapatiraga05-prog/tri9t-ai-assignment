from fastapi import FastAPI

from app.api import document_router, testcase_router, version_router
from app.database.init_db import init_db

app = FastAPI(title="Tri9T AI Assignment")

app.include_router(document_router)
app.include_router(version_router)
app.include_router(testcase_router)


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}
    