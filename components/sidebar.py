from flet import Column, Text, IconButton, Icons  # Change 'icons' to 'Icons'

def Sidebar():
    return Column(
        [
            Text("Menu", size=20, weight="bold"),
            IconButton(Icons.HOME, tooltip="Home"),  # Change 'icons.HOME' to 'Icons.HOME'
            IconButton(Icons.PERSON, tooltip="Employees"),  # Change 'icons.PERSON' to 'Icons.PERSON'
            IconButton(Icons.STATISTICS, tooltip="Statistics"),  # Change 'icons.STATISTICS' to 'Icons.STATISTICS'
        ],
        width=200,
        padding=10,
        bgcolor="#f5f5f5"
    )
