from db import get_connection

def show_all_students():
    query = """
    SELECT s.ФИО, s.Группа, k.Название as Кафедра
    FROM Студенты s
    JOIN Кафедры k ON s.id_кафедры = k.id
    """
    try:
        with get_connection() as conn:
            rows = conn.execute(query).fetchall() [cite: 265]
            if not rows:
                print("Данных нет.")
                return
            print(f"{'ФИО':<25} | {'Группа':<10} | {'Кафедра'}")
            print("-" * 50)
            for row in rows:
                print(f"{row['ФИО']:<25} | {row['Группа']:<10} | {row['Кафедра']}")
    except Exception as e:
        print(f"Ошибка отчета: {e}")