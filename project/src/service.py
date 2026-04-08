import sqlite3
from db import get_connection

def add_student(fio, group_name, dept_id):
    query = "INSERT INTO Студенты (ФИО, Группа, id_кафедры) VALUES (?, ?, ?)"
    try:
        with get_connection() as conn:
            conn.execute(query, (fio, group_name, dept_id))
            conn.commit() [cite: 210]
            print(f"Студент {fio} добавлен.")
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")