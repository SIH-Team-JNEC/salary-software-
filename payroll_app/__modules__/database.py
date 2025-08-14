import sqlite3

def get_connection():
    return sqlite3.connect("payroll.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    # Employee Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        mobile_no TEXT NOT NULL,
        employee_id_no TEXT UNIQUE NOT NULL,
        aadhaar_no TEXT UNIQUE NOT NULL,
        pan_no TEXT UNIQUE NOT NULL,
        hourly_rate REAL DEFAULT 0
    )
    """)

    # Attendance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id_no TEXT NOT NULL,
        date TEXT NOT NULL,
        hours_worked REAL NOT NULL,
        FOREIGN KEY(employee_id_no) REFERENCES employees(employee_id_no)
    )
    """)

    conn.commit()
    conn.close()


