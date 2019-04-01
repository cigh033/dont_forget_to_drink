import tkinter
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
root.withdraw()
root.attributes("-topmost", True)

messagebox.showwarning("Trinken","Trinken nicht vergessen!")