import flet as ft

def it_staff_page(page: ft.Page):
    page.title = "IT Staff"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    staff_text = ft.Text("Welcome to the IT Staff Page!", size=48)

    page.add(staff_text)
