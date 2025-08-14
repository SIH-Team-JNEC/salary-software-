import flet as ft
from dashboard.dashboard_page import dashboard_page
from database.database import add_user, get_users

add_user('john_doe', 'john@example.com', "AB+ve")

# Retrieve and print all users
users = get_users()
for user in users:
    print(f'ID: {user[0]}, Username: {user[1]}, Email: {user[2]}, Blood group: {user[3]}')


def main(page: ft.Page):
    page.title = "Simple Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def go_to_dashboard(e):
        page.clean()  # Clear the current page
        dashboard_page(page)  # Call the dashboard page function

    dashboard_button = ft.ElevatedButton(text="Go to Dashboard", on_click=go_to_dashboard)

    page.add(dashboard_button)

ft.app(target=main)