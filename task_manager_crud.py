from fastapi import HTTPException
def create_task(cursor, conn, title):
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title, ))
    conn.commit()
    task_id = cursor.lastrowid
    return {"id": task_id, "title": title, "completed": False}

def get_task(cursor):
    cursor.execute("SELECT *FROM tasks")
    tasks = cursor.fetchall()
    task = []
    for row in tasks:
        task.append({"id": row[0], "title": row[1], "completed": row[2]})
    return task 

def update_task(cursor, conn, task_id, title):
    cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, task_id))
    conn.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task updated"}

def delete_task(cursor, conn, task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id, ))
    conn.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} deleted"}

def complete_task(cursor, conn, task_id):
    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")    
    return {"message": f"Task {task_id} completed"}
    
    