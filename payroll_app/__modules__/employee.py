from database import get_connection

def add_employee(name, mobile_no, employee_id_no, aadhaar_no, pan_no, hourly_rate):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (name, mobile_no, employee_id_no, aadhaar_no, pan_no, hourly_rate)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, mobile_no, employee_id_no, aadhaar_no, pan_no, hourly_rate))
    conn.commit()
    conn.close()
    print("✅ Employee added successfully!")

def view_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE employee_id_no=?", (emp_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE employee_id_no=?", (emp_id,))
    conn.commit()
    conn.close()
    print("🗑️ Employee deleted successfully!")

