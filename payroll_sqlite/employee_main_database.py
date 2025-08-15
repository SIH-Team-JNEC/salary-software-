import sqlite3

DB_NAME = "employees.db"

def create_table():
    """Create the employee table if not exists"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            mobile_no TEXT,
            employee_id_no TEXT,
            aadhaar_no TEXT,
            pan_no TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_employee(name, mobile_no, employee_id_no, aadhaar_no, pan_no):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO employees (name, mobile_no, employee_id_no, aadhaar_no, pan_no) VALUES (?, ?, ?, ?, ?)",
              (name, mobile_no, employee_id_no, aadhaar_no, pan_no))
    conn.commit()
    conn.close()

def view_employees():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    rows = c.fetchall()
    conn.close()
    return rows

def update_employee(emp_id, name, mobile_no, employee_id_no, aadhaar_no, pan_no):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        UPDATE employees
        SET name=?, mobile_no=?, employee_id_no=?, aadhaar_no=?, pan_no=?
        WHERE id=?
    """, (name, mobile_no, employee_id_no, aadhaar_no, pan_no, emp_id))
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE id=?", (emp_id,))
    conn.commit()
    conn.close()
