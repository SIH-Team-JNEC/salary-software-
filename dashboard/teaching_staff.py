import flet as ft
import dashboard.entry_page as entry_page

def teaching_staff_page(page: ft.Page):
    page.title = "Teaching Staff"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Heading
    staff_text = ft.Text("Teaching Staff Records", size=30, weight="bold")

    # DataTable
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("DOB")),
            ft.DataColumn(ft.Text("Gender")),
            ft.DataColumn(ft.Text("Mobile No")),
            ft.DataColumn(ft.Text("Email Address")),
            ft.DataColumn(ft.Text("Aadhar No")),
            ft.DataColumn(ft.Text("PAN No")),
            ft.DataColumn(ft.Text("Department")),
            ft.DataColumn(ft.Text("Designation")),
            ft.DataColumn(ft.Text("Employee ID")),
            ft.DataColumn(ft.Text("Date of Joining")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("mahesh deshmukh")),
                    ft.DataCell(ft.Text("01-01-1985")),
                    ft.DataCell(ft.Text("Male")),
                    ft.DataCell(ft.Text("9876543210")),
                    ft.DataCell(ft.Text("mahesh@example.com")),
                    ft.DataCell(ft.Text("1234-5678-9012")),
                    ft.DataCell(ft.Text("ABCDE1234F")),
                    ft.DataCell(ft.Text("Computer Science")),
                    ft.DataCell(ft.Text("Professor")),
                    ft.DataCell(ft.Text("EMP001")),
                    ft.DataCell(ft.Text("15-06-2010")),
                ]
            )
        ],
    )

    # Buttons
    def switch_entry_page(e):
        page.clean()
        entry_page.entry_pg(page)
    add_btn = ft.ElevatedButton("Add", icon=ft.Icons.ADD, bgcolor=ft.Colors.BLUE, color="white" , on_click=switch_entry_page)
    edit_btn = ft.ElevatedButton("Edit", icon=ft.Icons.EDIT, bgcolor=ft.Colors.YELLOW, color="black" )
    delete_btn = ft.ElevatedButton("Delete", icon=ft.Icons.DELETE, bgcolor=ft.Colors.RED, color="white")

# Wrap table inside a horizontally scrollable container
    data_table = ft.Row(
        [data_table],
        scroll="always",   # enables horizontal scrolling
        expand=1,
    )

    # Layout
    page.add( 
        staff_text,
        ft.Row([add_btn, edit_btn, delete_btn], alignment=ft.MainAxisAlignment.START, spacing=20),
        data_table
    )
    page.update()

    
