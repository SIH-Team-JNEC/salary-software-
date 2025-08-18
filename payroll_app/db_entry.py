import flet as ft
import sqlite3

def add_entry(entry_d):
    # add to table in database
    conn = sqlite3.connect("employees.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id_no TEXT PRIMARY KEY,
            name TEXT,
            dob TEXT,
            gender TEXT,
            mobile_no TEXT,
            email TEXT,
            address TEXT,
            aadhaar_no TEXT,
            pan_no TEXT,
            department TEXT,
            designation TEXT,
            date_of_joining TEXT
        )
    """)

    cur.execute("""
        INSERT OR REPLACE INTO employees (
            employee_id_no, name, dob, gender, mobile_no, email, address,
            aadhaar_no, pan_no, department, designation, date_of_joining
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        entry_d["employee_id_no"],
        entry_d["name"],
        entry_d["dob"],
        entry_d["gender"],
        entry_d["mobile_no"],
        entry_d["email"],
        entry_d["address"],
        entry_d["aadhaar_no"],
        entry_d["pan_no"],
        entry_d["department"],
        entry_d["designation"],
        entry_d["date_of_joining"]
    ))

    conn.commit()
    conn.close()
