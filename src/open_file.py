import tkinter as tk

from tkinter.filedialog import askopenfilename

import globals

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    globals.txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        globals.txt_edit.insert(tk.END, text)
    globals.window.title(f"Avi Takiyar - {filepath}")