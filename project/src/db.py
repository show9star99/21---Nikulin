import sqlite3
import os

# Настройка путей относительно папки src [cite: 116]
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database', 'university.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'database', 'schema.sql')

def get_connection():
    """Создает подключение к БД Университета [cite: 120]"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row # Позволяет обращаться по именам колонок [cite: 122]
    conn.execute("PRAGMA foreign_keys = ON;") # Включаем поддержку связей [cite: 123]
    return conn

def init_db():
    """Инициализирует базу по schema.sql [cite: 125]"""
    if not os.path.exists(SCHEMA_PATH):
        print(f"Ошибка! Схема не найдена по пути {SCHEMA_PATH}")
        return
    try:
        with get_connection() as conn:
            with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())
        print("--- База данных ИС Университет инициализирована ---")
    except sqlite3.Error as e:
        print(f"Ошибка при создании БД: {e}")