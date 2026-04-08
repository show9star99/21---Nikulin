import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database', 'university.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'database', 'schema.sql')


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    if not os.path.exists(SCHEMA_PATH):
        print(f"Error: {SCHEMA_PATH} not found")
        return

    with get_connection() as conn:
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
    print("Database initialized in /database folder.")


def add_student(name, group_id, dept_id):
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO Students (full_name, group_id, dept_id) VALUES (?, ?, ?)",
                (name, group_id, dept_id)
            )
            conn.commit()
            print("Success.")
    except Exception as e:
        print(f"Error: {e}")


def get_schedule_report():
    query = """
    SELECT s.day_of_week, s.subject_name, g.name as group_name, d.name as dept_name
    FROM Schedule s
    JOIN Groups g ON s.group_id = g.group_id
    JOIN Departments d ON g.dept_id = d.dept_id
    ORDER BY s.day_of_week;
    """
    with get_connection() as conn:
        return conn.execute(query).fetchall()


def main():
    init_db()

    while True:
        print("\n1. Schedule Report\n2. Add Student\n0. Exit")
        choice = input("> ")

        if choice == "1":
            data = get_schedule_report()
            for row in data:
                print(f"{row['day_of_week']} | {row['subject_name']} | {row['group_name']} | {row['dept_name']}")

        elif choice == "2":
            name = input("Name: ")
            g_id = int(input("Group ID: "))
            d_id = int(input("Dept ID: "))
            add_student(name, g_id, d_id)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()