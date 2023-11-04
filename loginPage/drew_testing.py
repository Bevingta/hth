from tkinter import *

root = Tk()
root.title("Calculate")
root.geometry("500x500")

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = sorted({'Good', 'Bad', 'Medium'})
tkvar.set('Good')  # set the default option

popupMenu = OptionMenu(root, tkvar, *choices)
Label(root, text="Please choose")
popupMenu.grid(row=3, column=2)
b2 = Button(root, text='Close', command=root.quit)

# on change dropdown value
def change_dropdown(*args):
    global dropdown
    dropdown = str(tkvar.get())
    print(dropdown)
    return dropdown

# link function to change dropdown
tkvar.trace('w', change_dropdown)

if tkvar.get == 'Good':
    print(5)

if tkvar.get == "Bad":
    print(10)

root.mainloop()