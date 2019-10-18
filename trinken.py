import tkinter
from tkinter import messagebox
import psutil

for proc in psutil.process_iter():
	if proc.name().lower() == "powerpnt.exe":
		hidden = True
		break
	else:
		hidden = False

# hide main window
root = tkinter.Tk()
root.withdraw()

if hidden == False:
	root.attributes("-topmost", True)
else:
	root.attributes("-topmost", False)
	
messagebox.showwarning("Trinken","Trinken nicht vergessen!")