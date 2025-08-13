from flet import Column, Text, ElevatedButton

def EmployeePage():
    return Column(
        [
            Text("Employee Management", size=24, weight="bold"),
            ElevatedButton("Add Employee", on_click=lambda e: print("Add Employee Clicked")),
            ElevatedButton("List Employees", on_click=lambda e: print("List Employees Clicked")),
        ],
        padding=20
    )

