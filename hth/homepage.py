#need button to the window of the Data Base
#need button to the question board


import tkinter as tk
from tkinter import ttk

from tkinter import messagebox



class DocumentDatabase:
    def __init__(self, root):
        self.root = root
        self.root.title("Document Data Base")



class QuestionBoard:

    def __init__(self, root):
        self.root = root
        self.root.title("Question Board")


class HomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Home Window")

        #Create Database button
        self.DatabaseButton = tk.Button(root, text = "Database Button", command = self.open_document_database)
        self.QuestionBoardButton = tk.Button(root, text = "Question Board Button", command = self.open_question_board)





    def open_document_database(self):
        database_root = tk.Toplevel(self.root)
        login_root.title("Document Data Base Title")


    def open_question_board(self):
        question_board_root = tk.Toplevel
        login_root.title("Question Board Title")
