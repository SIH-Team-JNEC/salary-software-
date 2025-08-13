from flet import Container, Text

def Footer():
    return Container(
        content=Text("Developed by Your Name | Version 1.0"),
        padding=10,
        bgcolor="#6200ea",
        color="white",
        alignment="center"
    )

