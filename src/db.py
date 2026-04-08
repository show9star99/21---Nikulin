import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_DIR = os.path.join(BASE_DIR, 'database')
DB_PATH = os.path.join(DATABASE_DIR, 'university.db')
SCHEMA_PATH = os.path.join(DATABASE_DIR, 'schema.sql')


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    if not os.path.exists(DATABASE_DIR):
        os.makedirs(DATABASE_DIR)

    if not os.path.exists(SCHEMA_PATH):
        print(f"Критическая ошибка: Файл {SCHEMA_PATH} не найден!")
        return

    try:
        with get_connection() as conn:
            with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())
        print("База данных успешно синхронизирована со схемой.")
    except sqlite3.Error as e:
        print(f"Ошибка при инициализации БД: {e}")