"""Entry point for the graphical application."""

from __future__ import annotations

from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


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

    REQUIRED_EXE = Path(
        r"C:\Users\Charlie\AppData\LocalLow\Meta\Horizon Worlds\Horizon.exe"
    )

    exe_frame = ttk.Frame(main_frame)
    exe_frame.pack(fill="x", pady=(0, 10))

    ttk.Label(exe_frame, text="Target executable:").grid(row=0, column=0, sticky="w")

    path_var = tk.StringVar(value=str(REQUIRED_EXE))
    validation_var = tk.StringVar(value="Waiting for Horizon.exe path…")

    path_entry = ttk.Entry(exe_frame, textvariable=path_var, width=42)
    path_entry.grid(row=1, column=0, sticky="ew", pady=(2, 0))
    exe_frame.columnconfigure(0, weight=1)

    def browse_for_exe() -> None:
        selection = filedialog.askopenfilename(
            title="Select Horizon.exe",
            filetypes=[("Executable", "Horizon.exe"), ("All files", "*.*")],
        )
        if selection:
            path_var.set(selection)

    ttk.Button(exe_frame, text="Browse…", command=browse_for_exe).grid(
        row=1, column=1, padx=(6, 0)
    )

    validation_label = ttk.Label(exe_frame, textvariable=validation_var)
    validation_label.grid(row=2, column=0, columnspan=2, sticky="w", pady=(4, 0))

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

    def current_exe_path() -> Path:
        return Path(path_var.get()).expanduser()

    def exe_is_valid(path: Path) -> bool:
        return path.is_file() and path.name.lower() == "horizon.exe"

    def refresh_validation(*_: object) -> None:
        candidate = current_exe_path()
        if exe_is_valid(candidate):
            validation_var.set("✔ Horizon.exe detected – ready to inject.")
            start_button.config(state="normal")
        else:
            validation_var.set(
                "⚠ Horizon.exe not found. Update the path before starting."
            )
            start_button.config(state="disabled")

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
        candidate = current_exe_path()
        if not exe_is_valid(candidate):
            messagebox.showerror(
                "Executable missing",
                "Please select a valid Horizon.exe before starting the loader.",
            )
            refresh_validation()
            return

        start_button.config(state="disabled")
        progress_var.set(0)
        log_text.configure(state="normal")
        log_text.delete("1.0", "end")
        log_text.configure(state="disabled")
        status_var.set("Initializing...")
        log(f"Injecting overlay into: {candidate}")
        root.after(200, lambda: run_step(0))

    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill="x", pady=(12, 0))

    start_button = ttk.Button(button_frame, text="Start", command=start_sequence)
    start_button.pack(side="left")
    start_button.config(state="disabled")

    ttk.Button(button_frame, text="Close", command=root.destroy).pack(side="right")

    refresh_validation()

    root.mainloop()


if __name__ == "__main__":
    launch()
