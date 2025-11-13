# Gland Executor

This repository provides a minimal graphical launcher that can be bundled into a
self-contained Windows executable.

## Downloading the project

1. **Open the correct terminal.** On Windows, press `⊞ Win`, type
   “PowerShell”, and open *Windows PowerShell* (or *Command Prompt*). _Do not_
   run these commands inside the Python REPL prompt that starts with `>>>`—that
   will raise `SyntaxError: invalid syntax`.
2. **Clone the repository** (replace the placeholder URL with the actual HTTPS
   or SSH address of your fork/remote):

   ```powershell
   git clone https://example.com/your-account/Gland-executor.git
   ```

3. **Change into the project directory.** On Windows PowerShell that does not
   support `&&` as a command separator, run this as a second command:

   ```powershell
   Set-Location Gland-executor
   ```

> **Tip:** If you download the ZIP instead of cloning, simply extract it and
> `cd`/`Set-Location` into the extracted `Gland-executor` folder before
> continuing.

## Requirements

Install the Python dependencies, which now include PyInstaller for packaging the
application. The `py -3 -m pip` form ensures Windows uses your latest Python 3
installation:

```powershell
py -3 -m pip install -r requirements.txt
```

## Running the application

To run the GUI directly with Python, execute the launcher script from the
repository root (again using `py -3` on Windows):

```powershell
py -3 main.py
```

> **Troubleshooting tip:** If you still see `SyntaxError: invalid syntax`, you
> are likely inside the interactive Python prompt. Type `exit()` and press
> `Enter` to leave the interpreter, then rerun the command from PowerShell or
> Command Prompt.

## Building a standalone executable

The project can be packaged into a single-file executable using PyInstaller.
From the repository root, run:

```powershell
py -3 -m PyInstaller --noconfirm --onefile --noconsole --name GlandExecutorLoader main.py
```

The resulting `GlandExecutorLoader.exe` will be available in the `dist/`
directory. Launch the executable to start the GUI without requiring a Python
installation.
