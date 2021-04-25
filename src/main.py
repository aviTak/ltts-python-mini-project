import tkinter as tk

from open_file import *
from save_file import *

import globals 
 
if __name__ == "__main__": 
    globals.initialize() 

globals.window.title("Avi Takiyar")
globals.window.rowconfigure(0, minsize=800, weight=1)
globals.window.columnconfigure(1, minsize=800, weight=1)

#txt_edit = tk.Text(window)

fr_buttons = tk.Frame(globals.window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
globals.txt_edit.grid(row=0, column=1, sticky="nsew")

globals.window.mainloop()