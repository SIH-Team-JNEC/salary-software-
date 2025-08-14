import flet as ft

def dashboard_page(page: ft.Page):
    page.title = "Dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    dashboard_text = ft.Text("Welcome to the Dashboard!", size=48)

    page.add(dashboard_text)
