import tkinter as tk
from login_page.ui.login_page_ui import LoginPage

# 🪟 Make a window
window = tk.Tk()
window.title("My First GUI")

# 🏷️ Add a label
label = tk.Label(window, text="Hello! I'm a label!")
label.pack()

# 🔘 Add a button that changes the label
def on_button_click():
    label.config(text="You clicked the button!")

button = tk.Button(window, text="Click me!", command=on_button_click)
button.pack()

# 🏁 Show the window
window.mainloop()
