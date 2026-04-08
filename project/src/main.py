import sys
from db import init_db
from services import add_student
from reports import show_all_students


def main():
    init_db()[cite: 159]
    while True:
        print("\n1. Список студентов\n2. Добавить студента\n0. Выход")
        choice = input("Выбор: ")

        if choice == "1":
            show_all_students()[cite: 294]
        elif choice == "2":
            fio = input("ФИО: ")
            grp = input("Группа: ")
            dep = input("ID кафедры: ")
            add_student(fio, grp, int(dep))[cite: 298]
        elif choice == "0":
            break
        else:
            print("Ошибка ввода.")


if __name__ == "__main__":
    main()