import tkinter as tk

from tkinter.filedialog import asksaveasfilename

import globals

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = globals.txt_edit.get(1.0, tk.END)
        output_file.write(text)
    globals.window.title(f"Avi Takiyar - {filepath}")