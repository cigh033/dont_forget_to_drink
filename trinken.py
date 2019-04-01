import tkinter
from tkinter import messagebox
import subprocess

startupinfo = None

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

proc = subprocess.run("powershell -command $ProcessActive = Get-Process powerpnt -ErrorAction SilentlyContinue;if($ProcessActive -eq $null){exit 1}else{exit 2}",startupinfo=startupinfo)
 

# hide main window
root = tkinter.Tk()
root.withdraw()
root.attributes("-topmost", True)


# message box display
if proc.returncode == 1:
	messagebox.showwarning("Trinken","Trinken nicht vergessen!")