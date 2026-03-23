from fastapi import FastAPI
from task_manager_db import cursor, conn
from routers import tasks

app = FastAPI()
app.include_router(tasks.router)
