from db import get_connection
import sqlite3

def add_student(fio, group_id):
    query = "INSERT INTO Students (full_name, group_id) VALUES (?, ?)"
    try:
        with get_connection() as conn:
            conn.execute(query, (fio, group_id))
            conn.commit()
            print(f"Студент {fio} добавлен в базу.")
    except sqlite3.Error as e:
        print(f"Не удалось добавить студента: {e}")