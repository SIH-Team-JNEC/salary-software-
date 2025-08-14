from database import get_connection

def add_attendance(employee_id_no, date, hours_worked):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO attendance (employee_id_no, date, hours_worked)
        VALUES (?, ?, ?)
    """, (employee_id_no, date, hours_worked))
    conn.commit()
    conn.close()
    print("✅ Attendance added successfully!")

def view_attendance(employee_id_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, hours_worked FROM attendance WHERE employee_id_no=?", (employee_id_no,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def calculate_salary(employee_id_no):
    conn = get_connection()
    cursor = conn.cursor()

    # Get hourly rate
    cursor.execute("SELECT hourly_rate FROM employees WHERE employee_id_no=?", (employee_id_no,))
    rate_row = cursor.fetchone()
    if not rate_row:
        print("❌ Employee not found!")
        conn.close()
        return

    hourly_rate = rate_row[0]

    # Get total hours worked
    cursor.execute("SELECT SUM(hours_worked) FROM attendance WHERE employee_id_no=?", (employee_id_no,))
    total_hours = cursor.fetchone()[0] or 0

    conn.close()
    total_salary = hourly_rate * total_hours
    return total_hours, total_salary
