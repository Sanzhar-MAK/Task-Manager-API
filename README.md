# Task-Manager-API
My first api in Python - FastAPI

# Task Manager API

Simple backend API built with FastAPI and SQLite.

## Features
Create tasks\
Get all tasks\
Get task by ID\
Update task\
Delete task\
Mark task as completed

## Tech Stack
FastAPI
SQLite
Pydantic

## Endpoints
GET /tasks
GET /tasks/{id}
POST /tasks
PUT /tasks/{id}
DELETE /tasks/{id}
PATCH /tasks/{id}/complete

## Run project
uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000/docs
