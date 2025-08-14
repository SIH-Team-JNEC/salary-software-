import flet as ft

def non_teaching_staff_page(page: ft.Page):
    page.title = "Non-Teaching Staff"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    staff_text = ft.Text("Welcome to the Non-Teaching Staff Page!", size=48)

    page.add(staff_text)
