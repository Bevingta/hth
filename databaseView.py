import tkinter as tk
from tkinter import *


def on_button_click():
    # This function will be called when the button is clicked
    selected_option1 = dropdown1.get()
    selected_option2 = dropdown2.get()
    print(f"Grade: {selected_option2}, Subject: {selected_option1}")

# Create the main application window
root = tk.Tk()
root.title("Dropdowns and Button in a Horizontal Line")

# Create a frame to hold the widgets in a horizontal line
frame = tk.Frame(root)
frame.pack()

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

# Create a button
button = tk.Button(frame, text="Filter", command=on_button_click)
button.pack(side="left")

listbox = Listbox(root)

listbox.pack(fill=BOTH, expand = "true")

#add in the loop to go through the list of lists here
for values in range(100):
    rating = "Rating: " + str(values)
    listbox.insert(END, values, rating, "")

# Start the main loop
root.mainloop()