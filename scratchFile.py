from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from lists import grades, subjects
from tkinter import Listbox


import mongo # our file

class NewDocument:

    def submitted_doc(self, dropdown1, dropdown2, doc_file_entry):
        # This function will be called when the button is clicked
        selected_option1 = dropdown1.get()
        selected_option2 = dropdown2.get()
        print(f"Grade: {selected_option2}, Subject: {selected_option1}")
        print(f"Filepath: {doc_file_entry.get()}")
        result = mongo.insert_pdf(self.doc_name_entry.get(), doc_file_entry.get(), selected_option2, self.doc_name_entry.get(), selected_option1)
        


    def __init__(self, root, user):
        # Create a frame to hold the widgets in a horizontal line
        frame = tk.Frame(root)
        frame.pack()

        self.doc_name = tk.Label(frame, text="File Name")
        self.doc_name.pack(side="left")
        self.doc_name_entry = tk.Entry(frame)
        self.doc_name_entry.pack(side="left")

        self.doc_file_label = tk.Label(frame, text="Document Filepath")
        self.doc_file_label.pack(side="left")
        self.doc_file_entry = tk.Entry(frame)
        self.doc_file_entry.pack(side="left")


        # Create the first dropdown
        dropdown1 = tk.StringVar(root)
        # Dropdown menu options
        dropdown1.set(subjects[0])  # Set the default selection
        dropdown_menu1 = tk.OptionMenu(frame, dropdown1, *subjects)
        dropdown_menu1.pack(side="left")

        # Create the second dropdown
        dropdown2 = tk.StringVar(root)

        dropdown2.set(grades[0])  # Set the default selection
        dropdown_menu2 = tk.OptionMenu(frame, dropdown2, *grades)
        dropdown_menu2.pack(side="left")

        # Create a button
        button = tk.Button(frame, text="Submit Document", command=lambda: self.submitted_doc(dropdown1, dropdown2, self.doc_file_entry))
        button.pack(side="right")

class RatingApp:
    def __init__(self, root, ref):
        self.root = root
        self.root.title("Rating App")
        self.ref = ref
        self.rating = 0  # Initialize the rating to 0

        # Create and configure labels
        self.label = tk.Label(root, text="Rate this product:")
        self.label.pack()

        # Create and configure rating buttons
        self.rating_buttons = []
        for i in range(1, 6):
            button = tk.Button(root, text=str(i), command=lambda i=i: self.set_rating(i))
            button.config(width=2, height=1)
            button.pack(side=tk.LEFT, padx=10)
            self.rating_buttons.append(button)

        # Create a submit button
        self.submit_button = tk.Button(root, text="Submit Rating", command=self.submit_rating)
        self.submit_button.pack()

    def set_rating(self, rating):
        self.rating = rating
        for button in self.rating_buttons:
            button.config(state=tk.NORMAL)
        for button in self.rating_buttons[:rating]:
            button.config(state=tk.DISABLED)

    def submit_rating(self):
        if self.rating == 0:
            messagebox.showerror("Error", "Please select a rating.")
        else:
            messagebox.showinfo("Success", f"You have rated this product {self.rating} stars.")
            print(self.rating)
            mongo.add_rating(self.ref, self.rating)
            self.root.destroy()

class databaseScreen:
    widgets = []
    search_frames = []

    def download_document(self, title, ref):
        mongo.read_and_save_pdf(title + '.pdf', ref)

    def DestroyAllWidgets(self, _widgets):
        for widget in _widgets:
            widget.destroy()
        widgets = []

    def open_new_document_page(self):
        popup_doc = tk.Toplevel(self.root)
        self.document_popup = NewDocument(popup_doc, self.user)


    def open_ratings_page(self, ref):
        popup = tk.Toplevel(self.root)
        self.rating_popup = RatingApp(popup, ref)

    def on_button_click(self, dropdown1, dropdown2):
        # first, destroy all search_frames
        for f in self.search_frames:
            f.destroy()
        self.search_frames = []

        # This function will be called when the button is clicked
        selected_subject = dropdown1.get()
        selected_grade = dropdown2.get()
        print(f"selected_subject: {selected_subject}, selected_grade: {selected_grade}")

        
        # add in the loop to go through the list of lists here
        results = mongo.search_for_pdf(selected_subject, selected_grade)
        for result in results:
            for i in range(100):
                if (result["number_of_ratings"] != 0):
                    rating = str(int(result["rating"] / result["number_of_ratings"]))
                else:
                    rating = "0"
                title = "Title: " + result["title"]
                insert_text = f"{title} (Rating: {rating}/5)"
                print(insert_text)

                resultFrame = tk.Frame(self.canvasFrame)
                resultLabel = tk.Label(resultFrame, text=insert_text)
                resultButton = tk.Button(resultFrame, text="Rate", command=lambda: self.open_ratings_page(result["ref"]))
                resultLabel.pack(side="left")
                downloadButton = tk.Button(resultFrame, text="Download", command=lambda: self.download_document(result["title"], result["ref"]))
                resultButton.pack(side="right", expand=1)
                downloadButton.pack(side="right", expand=1)
                resultFrame.pack(fill="x", padx=10, pady=5, expand=1)
                self.search_frames.append(resultFrame)

        self.canvasFrame.update()
            

    def __init__(self, root, user):
        self.user = user # reference to the user thats logged in 
        self.root = root
        self.root.title("Document Database")

        # Create a frame to hold the widgets in a horizontal line
        frame = tk.Frame(root)
        frame.pack(expand=1)

        new_doc = tk.Button(frame, text="New Document", command=self.open_new_document_page)
        new_doc.pack(side=tk.TOP)

        # Create the first dropdown
        dropdown1 = tk.StringVar(root)


        # Create the second dropdown
        dropdown2 = tk.StringVar(root)

        dropdown1.set(subjects[0])  # Set the default selection
        dropdown_menu1 = tk.OptionMenu(frame, dropdown1, *subjects)
        dropdown_menu1.pack(side=tk.TOP)

        dropdown2.set(grades[0])  # Set the default selection
        dropdown_menu2 = tk.OptionMenu(frame, dropdown2, *grades)
        dropdown_menu2.pack(side=tk.TOP)


        self.filter_button = tk.Button(frame, text="Filter", command=lambda: self.on_button_click(dropdown1, dropdown2))
        self.filter_button.pack(side=tk.TOP)

        canvas = tk.Canvas(frame, height=500)
        canvas.pack(side=tk.BOTTOM, expand=1)

        scrollbar = tk.Scrollbar(root, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # frame inside to hold doc items
        self.canvasFrame = tk.Frame(frame)
        canvas.create_window(0,300, window=self.canvasFrame, anchor=tk.NW)

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        self.canvasFrame.bind("<Configure>", on_frame_configure)


class NewUserLoginWindow:
    widgets = []
    
    def user_pass_to_main(self):
        result = mongo.create(self.username_entry.get(), self.password_entry.get(), self.clicked_grade.get(), self.clicked_subject.get())
        if not result:
            print("Something went wrong with creating a new user!")
            unsuccessful = tk.Label(root, text="Uh Oh! Something went wrong with creating a new user")
            unsuccessful.pack()
        else:
            print("New user created successfully")
            successful = tk.Label(root, text="New User Successfully Created.")
            successful.pack()

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
            # label.config(text=clicked.get())
            label.config(text="Hello, World")

        # datatype of menu text
        self.clicked_subject = tk.StringVar(root)

        # initial menu text
        self.clicked_subject.set("Subject")

        # Create Dropdown menu
        selected_subject = tk.OptionMenu(root, self.clicked_subject, *subjects)
        selected_subject.pack()

        # on change dropdown value
        def change_dropdown_subject(*args):
            global dropdown
            dropdown = str(self.clicked_subject.get())
            print(dropdown)
            return dropdown

        # link function to change dropdown
        self.clicked_subject.trace('w', change_dropdown_subject)


        # Create Label
        label = tk.Label(root, text=" ")
        label.pack()

        # datatype of menu text
        self.clicked_grade = tk.StringVar()

        # initial menu text
        self.clicked_grade.set("Grade")

        # Create Dropdown menu
        drop = tk.OptionMenu(root, self.clicked_grade, *grades)
        drop.pack()

        def change_dropdown_grade(*args):
            global dropdown
            dropdown = str(self.clicked_grade.get())
            print(dropdown)
            return dropdown

        # link function to change dropdown
        self.clicked_grade.trace('w', change_dropdown_grade)

        # Create Label
        label = tk.Label(root, text=" ")
        label.pack()

        self.create_button = tk.Button(root, text="Create User", command=self.user_pass_to_main)
        self.create_button.pack()

        returnButton = tk.Button(root, text="Return to Login Screen", command=self.return_to_login)
        returnButton.pack(side=tk.BOTTOM)
        
        self.widgets.append(returnButton)
        self.widgets.append(self.username_label)
        self.widgets.append(self.username_entry)
        self.widgets.append(self.password_label)
        self.widgets.append(self.password_entry)
        self.widgets.append(drop)

    def return_to_login(self):
        for widget in self.widgets:
            try:
                widget.destroy()
            except:
                print("failed to destroy a widget")
        self.widget = []
        self.root.destroy()
        root = tk.Tk()
        root.geometry("1000x500")
        MainApplication(root)


class ExistingUserLoginWindow:
    widgets = []

    def user_pass_to_main(self, user):
        self.root.title("Main Window")

        self.DestroyAllWidgets(self.widgets)
        root = tk.Tk()
        root.geometry("1000x500")
        login_window = databaseScreen(root, user)

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
        self.widgets = []

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are correct (you can replace this with your own logic) (it has been replaced)
        user = mongo.validate_user(username, password)
        if user:
            print("Passed")
            self.user_pass_to_main(user)
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

        self.DestroyAllWidgets()
        login_window = ExistingUserLoginWindow(self.root)

    def open_new_user_login_page(self):
        self.root.title("New User")

        self.DestroyAllWidgets()
        login_window = NewUserLoginWindow(self.root)

    def DestroyAllWidgets(self):
        for widget in self.widgets:
            try:
                widget.destroy()
            except:
                print("failed to destroy a widget")
        self.widgets = [] # clear widgets

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
