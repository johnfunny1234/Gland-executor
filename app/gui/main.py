"""Entry point for the graphical application."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


def launch() -> None:
    """Launch a simple GUI window for demonstration purposes."""
    root = tk.Tk()
    root.title("Gland Executor")
    root.geometry("320x180")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill="both", expand=True)

    label = ttk.Label(
        main_frame,
        text="Gland Executor loader is running!",
        anchor="center",
        justify="center",
        font=("Segoe UI", 12),
    )
    label.pack(expand=True)

    ttk.Button(main_frame, text="Close", command=root.destroy).pack()

    root.mainloop()


if __name__ == "__main__":
    launch()
