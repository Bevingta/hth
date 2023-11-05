import tkinter as tk
from tkinter import *
import mongo

class Window:
    def __init__(self,parent):
        super().__init__(parent)
        self.root = root
        self.root.title = "New Document"

        # create a username
        self.document_name = tk.Label(root, text="Username: ")
        self.document_name.pack()
        self.document_name_entry = tk.Entry(root)
        self.document_name_entry.pack()


def on_button_click():
    # This function will be called when the button is clicked
    selected_option1 = dropdown1.get()
    selected_option2 = dropdown2.get()
    print(f"Grade: {selected_option2}, Subject: {selected_option1}")

    listbox.pack(fill=BOTH, expand=True)

    listbox.delete(0,listbox.size())

    # add in the loop to go through the list of lists here
    results = mongo.search_for_pdf(selected_option1, selected_option2)
    for result in results:
        if (result["number_of_ratings"] != 0):
            rating = str(result["rating"] / result["number_of_ratings"])
        else:
            rating = "0"
        title = "Title: " + result["title"]
        insert_text = f"{title} (Rating: {rating})"
        listbox.insert(END, insert_text, "")

# Create the main application window
root = tk.Tk()
root.title("Dropdowns and Button in a Horizontal Line")

root.geometry("1000x500")

# Create a frame to hold the widgets in a horizontal line
frame = tk.Frame(root)
frame.pack()

#not sure what you want here
def create_new_doc():
    window = Window
    window.grab_set()


new_doc_button = tk.Button(frame, text="Upload Document", command=create_new_doc)
new_doc_button.pack(side="left")

# Create the first dropdown
dropdown1 = tk.StringVar(root)
# Dropdown menu options
subject_filter = [
    "Math",
    "English",
    "Science",
    "History",
    "PE",
    "Art",
    "Chemistry",
    "Other"
]
dropdown1.set(subject_filter[0])  # Set the default selection
dropdown_menu1 = tk.OptionMenu(frame, dropdown1, *subject_filter)
dropdown_menu1.pack(side="left")

# Create the second dropdown
dropdown2 = tk.StringVar(root)
# Dropdown menu options
grade_filter = [
    "1st",
    "2nd",
    "3rd",
    "4th",
    "5th",
    "6th",
    "7th",
    "8th",
    "Freshmen (High School)",
    "Sophomore (High School)",
    "Junior (High School)",
    "Senior (High School)",
    "Freshmen (College)",
    "Sophomore (College)",
    "Junior (College)",
    "Senior(College"
]
dropdown2.set(grade_filter[0])  # Set the default selection
dropdown_menu2 = tk.OptionMenu(frame, dropdown2, *grade_filter)
dropdown_menu2.pack(side="left")

listbox = Listbox(root)

# Create a button
button = tk.Button(frame, text="Filter", command=on_button_click)
button.pack(side="left")

# Start the main loop
root.mainloop()

