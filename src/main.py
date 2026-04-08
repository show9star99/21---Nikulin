import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from db import init_db, get_connection
from services import add_student
from reports import show_all_students


def list_groups():
    print("\nДоступные группы (ID - Код):")
    with get_connection() as conn:
        groups = conn.execute("SELECT group_id, group_code FROM Groups").fetchall()
        for g in groups:
            print(f"{g['group_id']} - {g['group_code']}")


def main():
    init_db()
    while True:
        print("\n--- ИС УНИВЕРСИТЕТ ---")
        print("1. Показать список студентов")
        print("2. Добавить нового студента")
        print("0. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            show_all_students()
        elif choice == "2":
            list_groups()
            fio = input("Введите ФИО: ")
            g_id = input("Введите ID группы: ")
            add_student(fio, int(g_id))
        elif choice == "0":
            break
        else:
            print("Некорректный ввод.")


if __name__ == "__main__":
    main()