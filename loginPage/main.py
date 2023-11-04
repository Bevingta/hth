import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        # Create labels and entry fields for username and password
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")  # Use "show" to hide the password
        self.password_entry.pack()

        # Create a login button
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are correct (you can replace this with your own logic)
        if username == "your_username" and password == "your_password":
            messagebox.showinfo("Login Successful", "Welcome, " + username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Screen")

        # Create a button to open the login page
        self.login_button = tk.Button(root, text="Open Login Page", command=self.open_login_page)
        self.login_button.pack()

    def open_login_page(self):
        self.root.iconify()  # Hide the main screen
        login_root = tk.Toplevel(self.root)
        login_window = LoginWindow(login_root, self)

if __name__ == "__main__":
    root = tk.Tk()
    main_screen = MainScreen(root)
    root.mainloop()


