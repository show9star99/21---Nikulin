import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'database', 'university.db') [cite: 117]
SCHEMA_PATH = os.path.join(BASE_DIR, 'database', 'schema.sql') [cite: 118]

def get_connection():
    conn = sqlite3.connect(DB_PATH) [cite: 121]
    conn.row_factory = sqlite3.Row [cite: 122]
    conn.execute("PRAGMA foreign_keys = ON;") [cite: 123]
    return conn

def init_db():
    if not os.path.exists(SCHEMA_PATH):
        return
    try:
        with get_connection() as conn:
            with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
                conn.executescript(f.read()) [cite: 133]
    except sqlite3.Error:
        pass