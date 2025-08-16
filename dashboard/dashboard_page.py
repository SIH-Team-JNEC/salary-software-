import flet as ft
import dashboard.teaching_staff as teaching_staff
import dashboard.non_teaching_staff as non_teaching_staff
import dashboard.cleaning_staff as cleaning_staff
import dashboard.accounting_staff as accounting_staff
import dashboard.it_staff as it_staff

def dashboard_page(page: ft.Page):
    page.title = "Dashboard"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    dashboard_text = ft.Text("Welcome to the Dashboard!", size=48) 
    
    def teaching_staff_page(e):
        page.clean()
        teaching_staff.teaching_staff_page(page)
    dashboard_button1 = ft.ElevatedButton(text="teaching staff", on_click=teaching_staff_page)
    

    def non_teaching_staff_page(e):
        page.clean()
        non_teaching_staff.non_teaching_staff_page(page)
    dashboard_button2 = ft.ElevatedButton(text="non-teaching staff", on_click=non_teaching_staff_page)
    
    def cleaning_staff_page(e):
        page.clean()
        cleaning_staff.cleaning_staff_page(page)
    dashboard_button3 = ft.ElevatedButton(text="cleaning staff", on_click=cleaning_staff_page)

    def accounting_staff_page(e):
        page.clean()
        accounting_staff.accounting_staff_page(page)
    dashboard_button4 = ft.ElevatedButton(text="accounting staff", on_click=accounting_staff_page)

    def it_staff_page(e):
        page.clean()
        it_staff.it_staff_page(page)
    dashboard_button5 = ft.ElevatedButton(text="IT staff", on_click=it_staff_page)

    page.add(dashboard_text, dashboard_button1, dashboard_button2, dashboard_button3, dashboard_button4, dashboard_button5)