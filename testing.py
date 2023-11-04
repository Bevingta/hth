import tkinter as tk

def download_document(document_name):
    # Replace this function with your own download logic
    # In this example, we simply print the document name
    print(f"Downloading document: {document_name}")

root = tk.Tk()
root.title("Document List")

# Create a canvas with a vertical scrollbar
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="left", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the document items
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Create a list of documents (replace this with your actual document data)
documents = [
    "Document 1",
    "Document 2",
    "Document 3",
    "Document 4",
    "Document 5",
]

# Function to add document items with download buttons
def add_document_items():
    for document_name in documents:
        document_frame = tk.Frame(frame)
        document_frame.pack(fill="x", padx=10, pady=5, expand = "true")

        document_label = tk.Label(document_frame, text=document_name)
        document_label.pack(side="left")

        download_button = tk.Button(document_frame, text="Download", command=lambda name=document_name: download_document(name))
        download_button.pack(side="right", expand = "true")

add_document_items()

# Update the canvas when the frame size changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

root.mainloop()