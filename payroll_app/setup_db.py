# setup_db.py
import sqlite3
from pathlib import Path
def steup_database():
    DB_PATH = Path(__file__).parent / "payroll.db"
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        dob TEXT,
        gender TEXT,
        mobile_no TEXT NOT NULL,
        email TEXT,
        address TEXT,
        aadhaar_no TEXT,
        pan_no TEXT,
        department TEXT,
        designation TEXT,
        employee_id_no TEXT UNIQUE NOT NULL,
        date_of_joining TEXT
    )
    """)

    # Sample data (run only first time)
    cur.execute("SELECT COUNT(*) FROM employees")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            """INSERT INTO employees
            (name, dob, gender, mobile_no, email, address, aadhaar_no, pan_no,
             department, designation, employee_id_no, date_of_joining)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            [
                ("Sayali Joshi","1998-05-01","Female","9876543210","sayali@example.com","Pune",
                 "1234-5678-9012","ABCDE1234F","HR","HR Executive","EMP001","2021-04-12"),
                ("Rahul Sharma","1996-08-12","Male","9123456789","rahul@example.com","Mumbai",
                 "2345-6789-0123","PQRSX5678Y","Finance","Accountant","EMP002","2020-06-20"),
                ("Aditi Patil","1999-11-20","Female","9988776655","aditi@example.com","Nashik",
                 "3456-7890-1234","LMNOP1234Z","IT","Software Engineer","EMP003","2022-01-10"),
            ]
        )

    conn.commit()
    conn.close()
    print(f"DB ready at: {DB_PATH}")