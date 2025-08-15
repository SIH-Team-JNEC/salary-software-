import payroll_sqlite.employee_main_database as db

def main():
    db.create_table()

    while True:
        print("\nPayroll App - Employee Database")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            mobile_no = input("Enter Mobile No: ")
            employee_id_no = input("Enter Employee ID No: ")
            aadhaar_no = input("Enter Aadhaar No: ")
            pan_no = input("Enter PAN No: ")
            db.add_employee(name, mobile_no, employee_id_no, aadhaar_no, pan_no)
            print("Employee Added!")

        elif choice == "2":
            employees = db.view_employees()
            for emp in employees:
                print(emp)

        elif choice == "3":
            emp_id = int(input("Enter Employee ID to update: "))
            name = input("Enter New Name: ")
            mobile_no = input("Enter New Mobile No: ")
            employee_id_no = input("Enter New Employee ID No: ")
            aadhaar_no = input("Enter New Aadhaar No: ")
            pan_no = input("Enter New PAN No: ")
            db.update_employee(emp_id, name, mobile_no, employee_id_no, aadhaar_no, pan_no)
            print("Employee Updated!")

        elif choice == "4":
            emp_id = int(input("Enter Employee ID to delete: "))
            db.delete_employee(emp_id)
            print("Employee Deleted!")

        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main() 
