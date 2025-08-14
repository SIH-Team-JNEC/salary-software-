import flet as ft

def teaching_staff_page(page: ft.Page):
    page.title = "Teaching Staff"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    staff_text = ft.Text("Welcome to the Teaching Staff Page!", size=48)

    page.add(staff_text)

    
