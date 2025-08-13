from flet import Column, Text, IconButton, Icons  # Ensure you have the correct import

def Sidebar():
    return Column(
        [
            Text("Menu", size=20, weight="bold"),
            IconButton(Icons.HOME, tooltip="Home"),
            IconButton(Icons.PERSON, tooltip="Employees"),
            IconButton(Icons.CHART, tooltip="Statistics"),  # Replace with a valid icon
        ],
        width=200,
        padding=10,
        bgcolor="#f5f5f5"
    )

