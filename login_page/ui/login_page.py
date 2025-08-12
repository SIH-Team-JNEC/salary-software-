import tkinter as tk

class LoginPage:
    def __init__.py:
        self.master = master
        self.master.title = ("Login Page")

        self.label_username = tk.Label(master, text="Username")
        self.label_username.pack()

        self.entry_username = tk.Entry(master)
        self.entry_username.pack()

        self.label_password = tk.Label(master, text="Password")
        self.label_password.pack()

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.button_login.pack()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Simple validation (replace with your own logic)
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Success", "Welcome to the Dashboard!")
            self.master.destroy()  # Close the login window
            self.open_dashboard()  # Open the dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def open_dashboard(self):
        from dashboard import Dashboard  # Import the Dashboard class
        dashboard_window = tk.Tk()
        Dashboard(dashboard_window)
        dashboard_window.mainloop()
