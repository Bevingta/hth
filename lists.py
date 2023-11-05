# Dropdown menu options
grades = [
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
    "Senior (College)"
]

subjects = [
    "Math",
    "English",
    "Science",
    "History",
    "PE",
    "Art",
    "Chemistry",
    "Other"
]

class databaseScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Database")

        def on_button_click(self):
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
        dropdown_menu1 = tk.OptionMenu(frame, dropdown1, *subjects)
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
        dropdown_menu2 = tk.OptionMenu(frame, dropdown2, *grades)
        dropdown_menu2.pack(side="left")

        listbox = Listbox(root)

        # Create a button
        filter_button = tk.Button(frame, text="Filter", command=on_button_click)

        filter_button.pack(side="left")


    def user_pass_to_main(self):
        self.root.title("Main Window")

        self.DestroyAllWidgets(self.widgets)

        login_window = databaseScreen(self.root)