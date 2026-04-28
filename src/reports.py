from db import get_connection


def show_all_students():
    # Добавляем s.student_id в SELECT
    query = """
    SELECT s.student_id, s.full_name, g.group_code, g.course
    FROM Students s
    JOIN Groups g ON s.group_id = g.group_id
    """
    try:
        with get_connection() as conn:
            rows = conn.execute(query).fetchall()
            if not rows:
                print("В базе пока нет записей о студентах.")
                return

            # Добавляем колонку ID в заголовок
            print(f"\n{'ID':<4} | {'ФИО':<25} | {'ГРУППА':<10} | {'КУРС'}")
            print("-" * 55)
            for row in rows:
                print(f"{row['student_id']:<4} | {row['full_name']:<25} | {row['group_code']:<10} | {row['course']}")
    except Exception as e:
        print(f"Ошибка при формировании отчета: {e}")