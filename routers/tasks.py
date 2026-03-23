from fastapi import APIRouter, Depends
import task_manager_crud
from task_manager_db import get_db
from task_manager_schemas import TaskCreate, TaskResponse


router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db = Depends(get_db)):
    cursor, conn = db
    return task_manager_crud.create_task(cursor, conn, task.title)

@router.get("/tasks", response_model=list[TaskResponse])
def get_task(db = Depends(get_db)):
    cursor, _ = db
    return task_manager_crud.get_task(cursor)

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, db = Depends(get_db)):
    cursor, conn = db
    return task_manager_crud.update_task(cursor, conn, task_id, task.title)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db = Depends(get_db)):
    cursor, conn = db
    return task_manager_crud.delete_task(cursor, conn, task_id)

@router.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int, db = Depends(get_db)):
    cursor, conn = db
    return task_manager_crud.complete_task(cursor, conn, task_id)