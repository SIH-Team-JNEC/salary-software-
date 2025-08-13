from flet import Column, Text

def MainPage():
    return Column(
        [
            Text("Dashboard Statistics", size=24, weight="bold"),
            Text("Total Employees: 100"),
            Text("Active Projects: 5"),
            Text("Pending Tasks: 20"),
        ],
        padding=20
    )

