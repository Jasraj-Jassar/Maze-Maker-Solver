import tkinter as tk
from tkinter import messagebox
import parameters

def get_settings():
    root = tk.Tk()
    root.title("Maze Solver Setup")
    root.resizable(False, False)

    size_var = tk.StringVar(value=str(parameters.row))
    mode_var = tk.IntVar(value=1)
    result = {"size": None, "mode": None}

    tk.Label(root, text="Grid size (N for NxN)").grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")
    size_entry = tk.Entry(root, textvariable=size_var, width=8)
    size_entry.grid(row=1, column=0, padx=12, pady=(0, 10), sticky="w")
    size_entry.focus()

    tk.Label(root, text="Select mode").grid(row=2, column=0, padx=12, pady=(0, 4), sticky="w")
    modes = [
        ("Manual Mode (Control with keyboard)", 1),
        ("Random Mode (Basic random movement)", 2),
        ("Smarter Random Mode (Enhanced random movement)", 3),
        ("Dijkstra Mode (Shortest path)", 4),
    ]
    for idx, (label, value) in enumerate(modes, start=3):
        tk.Radiobutton(root, text=label, variable=mode_var, value=value).grid(
            row=idx, column=0, padx=12, pady=2, sticky="w"
        )

    def start():
        raw = size_var.get().strip()
        try:
            size = int(raw)
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")
            return

        if size < 2:
            messagebox.showerror("Invalid input", "Grid size must be at least 2")
            return

        result["size"] = size
        result["mode"] = mode_var.get()
        root.destroy()

    def on_close():
        root.destroy()

    tk.Button(root, text="Start", command=start).grid(row=7, column=0, padx=12, pady=12, sticky="e")
    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

    return result["size"], result["mode"]
