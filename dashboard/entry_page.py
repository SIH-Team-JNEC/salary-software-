import flet as ft
import dashboard.dashboard_page as dbpg

def save_to_db(data, page: ft.Page):
  page.add(ft.Text("Done"))

def entry_pg(page: ft.Page):
    page.title = "Input Fields Example"
    
    # Create a list to hold input fields
    input_fields = []
    
    def back_to_dashboard(page: ft.Page):
        page.clear()
        dbpg.dashboard_page(page)
    
    # Function to add input fields
    def add_input_field(e):
        input_field = ft.TextField(label=f"Input {len(input_fields) + 1}")
        input_fields.append(input_field)
        page.add(input_field)

    # Function to handle form submission
    def submit_form(e):
        for field in input_fields:
            if field.value:
                save_to_db(field.value, page)
        page.add(ft.Text("Data saved to database!"))

    # Button to add more input fields
    add_button = ft.ElevatedButton("Add Input Field", on_click=add_input_field)
    
    # Submit button
    submit_button = ft.ElevatedButton("Submit", on_click=submit_form)

    # Add initial button and submit button to the page
    page.add(add_button, submit_button)
ft.app(target=entry_pg)