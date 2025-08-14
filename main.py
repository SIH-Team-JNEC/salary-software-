from payroll_app.database import create_table
import payroll_app.employee
import payroll_app.attendance

def main():
    create_table()

    while True:
        print("\n=== Payroll System ===")
        print("1. Add Employee")
        print("2. View All Employees")
        
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Add Attendance")
        print("6. View Attendance")
        print("7. Calculate Salary")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            mobile_no = input("Enter mobile no: ")
            employee_id_no = input("Enter Employee ID: ")
            aadhaar_no = input("Enter Aadhaar No: ")
            pan_no = input("Enter PAN No: ")
            hourly_rate = float(input("Enter hourly rate: "))
            employee.add_employee(name, mobile_no, employee_id_no, aadhaar_no, pan_no, hourly_rate)

        elif choice == "2":
            for emp in employee.view_employees():
                print(emp)

        elif choice == "3":
            emp_id = input("Enter Employee ID to search: ")
            emp = employee.search_employee(emp_id)
            if emp:
                print(emp)
            else:
                print("Employee not found!")

        elif choice == "4":
            emp_id = input("Enter Employee ID to delete: ")
            employee.delete_employee(emp_id)

        elif choice == "5":
            emp_id = input("Enter Employee ID: ")
            date = input("Enter date (YYYY-MM-DD): ")
            hours = float(input("Enter hours worked: "))
            attendance.add_attendance(emp_id, date, hours)

        elif choice == "6":
            emp_id = input("Enter Employee ID: ")
            records = attendance.view_attendance(emp_id)
            for rec in records:
                print(f"Date: {rec[0]}, Hours: {rec[1]}")

        elif choice == "7":
            emp_id = input("Enter Employee ID: ")
            total_hours, total_salary = attendance.calculate_salary(emp_id)
            print(f"Total Hours Worked: {total_hours}")
            print(f"Total Salary: ₹{total_salary}")

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()

