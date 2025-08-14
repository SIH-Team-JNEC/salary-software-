import flet as ft

def accounting_staff_page(page: ft.Page):
    page.title = "Accounting Staff"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    staff_text = ft.Text("Welcome to the Accounting Staff Page!", size=48)

    page.add(staff_text)
