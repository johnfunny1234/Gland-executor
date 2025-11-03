# Gland Executor

This repository provides a minimal graphical launcher that can be bundled into a
self-contained Windows executable.

## Requirements

Install the Python dependencies, which now include PyInstaller for packaging the
application:

```bash
pip install -r requirements.txt
```

## Running the application

To run the GUI directly with Python, execute:

```bash
python main.py
```

## Building a standalone executable

The project can be packaged into a single-file executable using PyInstaller.
From the repository root, run:

```bash
pyinstaller --noconfirm --onefile --noconsole --name GlandExecutorLoader main.py
```

The resulting `GlandExecutorLoader.exe` will be available in the `dist/`
directory. Launch the executable to start the GUI without requiring a Python
installation.
