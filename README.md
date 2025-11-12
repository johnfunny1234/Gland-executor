# Gland Executor

This repository provides a minimal graphical launcher that can be bundled into a
self-contained Windows executable.

## Downloading the project

Clone the repository (replace the placeholder URL with the actual HTTPS or SSH
address of your fork/remote):

```powershell
git clone https://example.com/your-account/Gland-executor.git
```

Then change into the project directory. On Windows PowerShell that does not
support `&&` as a command separator, run this as a second command:

```powershell
Set-Location Gland-executor
```

> **Tip:** If you download the ZIP instead of cloning, simply extract it and
> `cd`/`Set-Location` into the extracted `Gland-executor` folder before
> continuing.

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
