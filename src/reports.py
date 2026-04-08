from db import get_connection


def show_all_students():
    query = """
    SELECT s.full_name, g.group_code, g.course
    FROM Students s
    JOIN Groups g ON s.group_id = g.group_id
    """
    try:
        with get_connection() as conn:
            rows = conn.execute(query).fetchall()
            if not rows:
                print("В базе пока нет записей о студентах.")
                return

            print(f"\n{'ФИО':<25} | {'ГРУППА':<10} | {'КУРС'}")
            print("-" * 50)
            for row in rows:
                print(f"{row['full_name']:<25} | {row['group_code']:<10} | {row['course']}")
    except Exception as e:
        print(f"Ошибка при формировании отчета: {e}")