import flet as ft
from dashboard.dashboard_page import dashboard_page

def main(page: ft.Page):
    page.title = "Simple Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def go_to_dashboard(e):
        page.clean()  # Clear the current page
        dashboard_page(page)  # Call the dashboard page function

    dashboard_button = ft.ElevatedButton(text="Go to Dashboard", on_click=go_to_dashboard)

    page.add(dashboard_button)

ft.app(target=main)