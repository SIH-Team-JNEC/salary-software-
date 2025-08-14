import flet as ft

def cleaning_staff_page(page: ft.Page):
    page.title = "Cleaning Staff"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    staff_text = ft.Text("Welcome to the Cleaning Staff Page!", size=48)

    page.add(staff_text)
