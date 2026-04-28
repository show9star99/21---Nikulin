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


def delete_student(student_id):
    query = "DELETE FROM Students WHERE student_id = ?"
    try:
        with get_connection() as conn:
            # Проверяем, существует ли студент
            cursor = conn.execute("SELECT full_name FROM Students WHERE student_id = ?", (student_id,))
            student = cursor.fetchone()

            if student:
                conn.execute(query, (student_id,))
                conn.commit()
                print(f"Студент {student['full_name']} (ID: {student_id}) успешно удален.")
            else:
                print(f"Студент с ID {student_id} не найден.")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении: {e}")