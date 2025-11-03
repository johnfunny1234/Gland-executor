"""GUI bootstrap for the Gland Executor Meta Horizon World loader."""
from __future__ import annotations

import tkinter as tk
from dataclasses import dataclass


@dataclass
class LoaderConfig:
    """Configuration settings for the Meta Horizon World GUI loader."""

    title: str = "Gland Executor Loader"
    width: int = 480
    height: int = 320


class LoaderApp:
    """Main application window for the Meta Horizon World GUI loader."""

    def __init__(self, root: tk.Tk, config: LoaderConfig | None = None) -> None:
        self.root = root
        self.config = config or LoaderConfig()
        self._configure_root()
        self._build_layout()

    def _configure_root(self) -> None:
        """Configure the base Tk root window."""
        self.root.title(self.config.title)
        self.root.geometry(f"{self.config.width}x{self.config.height}")
        self.root.resizable(False, False)

    def _build_layout(self) -> None:
        """Construct the placeholder layout for future loader features."""
        header = tk.Label(
            self.root,
            text="Meta Horizon World Loader",
            font=("Segoe UI", 16, "bold"),
        )
        header.pack(pady=(24, 12))

        description = tk.Label(
            self.root,
            text=(
                "Inject this module into Meta Horizon Worlds to launch the "
                "custom GUI overlay. Configure your modules, scripts, and "
                "automation hooks from here."
            ),
            wraplength=self.config.width - 40,
            justify="center",
        )
        description.pack(padx=20)

        status_frame = tk.LabelFrame(self.root, text="Loader Status")
        status_frame.pack(fill="both", expand=True, padx=20, pady=20)

        status_label = tk.Label(
            status_frame,
            text="Awaiting injection...",
            fg="orange",
            font=("Segoe UI", 12, "italic"),
        )
        status_label.pack(pady=16)

        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=(0, 20))

        tk.Button(control_frame, text="Inject", width=12, state=tk.DISABLED).pack(
            side=tk.LEFT, padx=5
        )
        tk.Button(control_frame, text="Configure", width=12, state=tk.DISABLED).pack(
            side=tk.LEFT, padx=5
        )

    def run(self) -> None:
        """Start the Tkinter main loop."""
        self.root.mainloop()


def launch(config: LoaderConfig | None = None) -> None:
    """Entry point used by the CLI wrapper to boot the loader GUI."""
    root = tk.Tk()
    app = LoaderApp(root, config=config)
    app.run()


__all__ = ["LoaderApp", "LoaderConfig", "launch"]
