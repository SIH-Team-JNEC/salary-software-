from flet import Page, Column, Row
from components.header import Header
from components.sidebar import Sidebar
from components.footer import Footer
from pages.main_page import MainPage
from pages.employee_page import EmployeePage

def main(page: Page):
    page.title = "Admin Dashboard"
    page.vertical_alignment = "start"

    header = Header()
    sidebar = Sidebar()
    main_page = MainPage()
    employee_page = EmployeePage()

    page.add(
        Column([
            header,
            Row([sidebar, main_page], expand=True),
            Footer()
        ], expand=True)
    )

if __name__ == "__main__":
    import flet as ft
    ft.app(target=main)
