
import sqlite3

def connect_db():
    return sqlite3.connect("defects.db", check_same_thread=False)

def create_table():
    conn = connect_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS defects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_reported TEXT,
            module TEXT,
            description TEXT,
            severity TEXT,
            status TEXT,
            assigned_to TEXT,
            resolution_date TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_defect(date_reported, module, description, severity, status, assigned_to, resolution_date):
    conn = connect_db()
    conn.execute("""
        INSERT INTO defects (
            date_reported, module, description,
            severity, status, assigned_to, resolution_date
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (date_reported, module, description, severity, status, assigned_to, resolution_date))
    conn.commit()
    conn.close()

def get_all_defects():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM defects")
    rows = cursor.fetchall()
    conn.close()
    return rows
