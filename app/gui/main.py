"""Entry point for the graphical application."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


def launch() -> None:
    """Launch the polished loader experience."""

    root = tk.Tk()
    root.title("Gland Executor")
    root.geometry("420x320")
    root.minsize(420, 320)
    root.resizable(False, False)

    style = ttk.Style(root)
    style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"))
    style.configure("Status.TLabel", font=("Segoe UI", 11))

    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill="both", expand=True)

    ttk.Label(main_frame, text="Gland Executor", style="Title.TLabel").pack(
        anchor="w"
    )
    ttk.Label(
        main_frame,
        text="Prepare the loader, then click Start to initialize the runtime.",
        padding=(0, 4, 0, 12),
    ).pack(anchor="w")

    status_var = tk.StringVar(value="Ready.")
    progress_var = tk.IntVar(value=0)

    status_label = ttk.Label(main_frame, textvariable=status_var, style="Status.TLabel")
    status_label.pack(anchor="w", fill="x")

    progress = ttk.Progressbar(
        main_frame,
        length=360,
        mode="determinate",
        maximum=5,
        variable=progress_var,
    )
    progress.pack(fill="x", pady=(6, 12))

    log_text = tk.Text(
        main_frame,
        width=40,
        height=8,
        state="disabled",
        wrap="word",
        relief="solid",
        borderwidth=1,
        font=("Consolas", 9),
    )
    log_text.pack(fill="both", expand=True)

    def log(message: str) -> None:
        log_text.configure(state="normal")
        log_text.insert("end", f"{message}\n")
        log_text.see("end")
        log_text.configure(state="disabled")

    steps = [
        "Scanning environment...",
        "Validating configuration...",
        "Preparing runtime components...",
        "Linking launcher modules...",
        "Finalizing loader state...",
    ]

    def run_step(index: int) -> None:
        if index >= len(steps):
            status_var.set("Loader ready – click Close to exit.")
            start_button.config(text="Loaded", state="disabled")
            log("✔ All systems ready.")
            return

        status_var.set(steps[index])
        log(f"• {steps[index]}")
        progress_var.set(index + 1)
        root.after(500, lambda: run_step(index + 1))

    def start_sequence() -> None:
        start_button.config(state="disabled")
        progress_var.set(0)
        log_text.configure(state="normal")
        log_text.delete("1.0", "end")
        log_text.configure(state="disabled")
        status_var.set("Initializing...")
        root.after(200, lambda: run_step(0))

    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill="x", pady=(12, 0))

    start_button = ttk.Button(button_frame, text="Start", command=start_sequence)
    start_button.pack(side="left")

    ttk.Button(button_frame, text="Close", command=root.destroy).pack(side="right")

    root.mainloop()


if __name__ == "__main__":
    launch()
