from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from lists import grades, subjects


import mongo # our file

class NewUserLoginWindow:
    widgets = []
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
        def show():
            label.config(text=clicked.get())

        # datatype of menu text
        clicked_subject = tk.StringVar(root)

        # initial menu text
        clicked_subject.set("Subject")

        # Create Dropdown menu
        selected_subject = tk.OptionMenu(root, clicked_subject, *subjects)
        selected_subject.pack()

        # on change dropdown value
        def change_dropdown(*args):
            global dropdown
            dropdown = str(clicked_subject.get())
            print(dropdown)
            return dropdown

        # link function to change dropdown
        clicked_subject.trace('w', change_dropdown)


        # Create Label
        label = tk.Label(root, text=" ")
        label.pack()

        # datatype of menu text
        clicked_grade = tk.StringVar()

        # initial menu text
        clicked_grade.set("Grade")

        # Create Dropdown menu
        drop = tk.OptionMenu(root, clicked_grade, *grades)
        drop.pack()

        def change_dropdown(*args):
            global dropdown
            dropdown = str(clicked_grade.get())
            print(dropdown)
            return dropdown

        # link function to change dropdown
        clicked_grade.trace('w', change_dropdown)

        # Create Label
        label = tk.Label(root, text=" ")
        label.pack()

        #this button is not showing up
        self.create_button = tk.button(root, text="Create User", command=self.user_pass_to_main)
        self.create_button.pack()

        self.widgets.append(self.username_label)
        self.widgets.append(self.username_entry)
        self.widgets.append(self.password_label)
        self.widgets.append(self.password_entry)
        self.widgets.append(dropdown)

class ExistingUserLoginWindow:
    widgets = []
    def __init__(self, root):
        self.root = root

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

        self.widgets.append(self.username_label)
        self.widgets.append(self.username_entry)
        self.widgets.append(self.password_label)
        self.widgets.append(self.password_entry)
        self.widgets.append(self.login_button)

    def DestroyAllWidgets(self, _widgets):
        for widget in _widgets:
            widget.destroy()
        widgets = []

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are correct (you can replace this with your own logic) (it has been replaced)
        if mongo.validate_user(username, password):
            print("Passed")
            self.user_pass_to_main()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

class MainApplication:
    widgets = []
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")

        # Set the initial window size
        self.root.geometry("1000x500")

        # Create a button to open the login page
        self.login_button = tk.Button(root, text="Existing User", command=self.open_existing_user_login_page)
        self.login_button.pack()
        self.widgets.append(self.login_button)

        self.login_new_button = tk.Button(root, text="New User", command=self.open_new_user_login_page)
        self.login_new_button.pack()
        self.widgets.append(self.login_new_button)

    def open_existing_user_login_page(self):
        self.root.title("Existing User Login")

        self.DestroyAllWidgets(self.widgets)

        login_window = ExistingUserLoginWindow(self.root)

    def open_new_user_login_page(self):
        self.root.title("New User")

        self.DestroyAllWidgets(self.widgets)

        login_window = NewUserLoginWindow(self.root)

    def DestroyAllWidgets(self, _widgets):
        for widget in _widgets:
            widget.destroy()
        widgets = []

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
