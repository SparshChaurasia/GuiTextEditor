import tkinter as tk
from tkinter import filedialog

OPENED_FILE = None


def update(event):
    cursor = textarea.index(tk.INSERT)
    row = cursor.split(".")[0]
    col = int(cursor.split(".")[-1]) + 1

    FILE_LENGTH.set(f"Ln {row}, Col {col}")


def save_file():
    if globals()[
        "OPENED_FILE"
    ]:  # If the file is saved for the first time and there is no path or title to the same
        with open(globals()["OPENED_FILE"].name, "w") as file:
            txt = textarea.get("1.0", "end-1c")
            file.write(txt)
            return

    # Returns a TextIOWrapper object with file name, mode and encoding
    with filedialog.asksaveasfile(
        mode="w",
        initialfile="Untitled.txt",
        defaultextension=".txt",
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
    ) as file:
        if file:  # If file is not None
            # Storing the file object in the OPENED_FILE variable and setting the
            globals()["OPENED_FILE"] = file
            FILE.set(file.name.split("/")[-1])
            # Storing the textarea contents and writing it into the file
            txt = textarea.get("1.0", "end-1c")
            file.write(txt)
            return


def open_file():
    with filedialog.askopenfile(
        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
    ) as file:  # Returns a TextIOWrapper object with file name, mode and encoding

        globals()["OPENED_FILE"] = file
        FILE.set(file.name.split("/")[-1])

        with open(
            file.name, "r"
        ) as f:  # Using the file name opening the file as python object

            # Storing the file contents and writing it in the textarea
            txt = f.read()
            textarea.delete("1.0", "end-1c")
            textarea.insert("1.0", txt)


root = tk.Tk()
root.title("TextEditor")
root.geometry("400x463")

FILE = tk.StringVar(root, "Unitiled")
FILE_LENGTH = tk.StringVar(root, "Ln -, Col -")

title_bar = tk.Label(root, textvariable=FILE, bg="white")
title_bar.pack(side=tk.TOP, fill=tk.X)

btn1 = tk.Button(title_bar, text="Save", command=save_file)
btn2 = tk.Button(title_bar, text="Open", command=open_file)
btn1.pack(side=tk.LEFT)
btn2.pack(side=tk.LEFT)

textarea = tk.Text(root, font=("Source Code Pro", 10))
textarea.pack(side=tk.TOP, fill=tk.BOTH)
textarea.bind("<KeyPress>", update)
textarea.bind("<KeyRelease>", update)

status_bar = tk.Label(root, textvariable=FILE_LENGTH, bg="white")
status_bar.pack(side=tk.TOP, fill=tk.X)

root.mainloop()
