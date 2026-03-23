import sqlite3

conn = sqlite3.connect("task_manager.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               completed BOOLEAN DEFAULT 0,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
               )
               """)

conn.commit()

def get_db():
    return cursor, conn       