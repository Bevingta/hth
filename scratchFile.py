import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import messagebox

import mongo # our file

class NewUserLoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("New User")

        #create a username
        self.username_label = tk.Label(root, text="Username: ")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        #create a password
        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root)
        self.password_entry.pack()

        #get the subject(dropdown menu)
        teacher_subject = tk.StringVar()
        dropdown = tk.OptionMenu(root, teacher_subject, "Option 1", "Option 2", "Option 3", "Option 4")
        dropdown.pack()

class ExistingUserLoginWindow:
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

        # Check if the username and password are correct (you can replace this with your own logic) (it has been replaced)
        if mongo.validate_user(username, password):
            messagebox.showinfo("Login Successful", "Welcome, " + username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        # Set the initial window size
        self.root.geometry("1000x500")

        # Create a button to open the login page
        self.login_button = tk.Button(root, text="Existing User", command=self.open_existing_user_login_page)
        self.login_button.pack()

        self.login_new_button = tk.Button(root, text="New User", command=self.open_new_user_login_page)
        self.login_new_button.pack()

    def open_existing_user_login_page(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title("Existing User Login")

        # Set the initial login window size
        self.root.geometry("1000x500")

        login_window = ExistingUserLoginWindow(self.root)

    def open_new_user_login_page(self):
        login_root = tk.Toplevel(self.root)
        login_root.title("New User Login")

        # Set the initial login window size
        login_root.geometry("1000x500")

        login_window = NewUserLoginWindow(login_root)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
