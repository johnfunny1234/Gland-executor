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
installation. If you specifically installed **Python 3.13**, substitute
`py -3.13` anywhere you see `py -3` so you explicitly target that interpreter:

```powershell
py -3 -m pip install -r requirements.txt
# or, on Python 3.13 specifically
py -3.13 -m pip install -r requirements.txt
```

## Running the application

To run the GUI directly with Python, execute the launcher script from the
repository root (again using `py -3`—or `py -3.13` if that is the version you
installed—on Windows):

```powershell
py -3 main.py
# or explicitly
py -3.13 main.py
```

> **Troubleshooting tip:** If you still see `SyntaxError: invalid syntax`, you
> are likely inside the interactive Python prompt. Type `exit()` and press
> `Enter` to leave the interpreter, then rerun the command from PowerShell or
> Command Prompt.

When the window opens you will see:

* A **Target executable** field that defaults to the Horizon Worlds installation
  path (`C:\Users\Charlie\AppData\LocalLow\Meta\Horizon Worlds\Horizon.exe`).
  Use the **Browse…** button if your copy is installed elsewhere. The Start
  button remains disabled until a valid `Horizon.exe` is detected, so the loader
  cannot “inject” until the dependency is present.
* A **Start** button that kicks off a short initialization sequence once the exe
  check passes, rather than immediately exiting with a “loaded” message.
* A status indicator, progress bar, and scrolling log so you can confirm each
  loader step completes successfully.

After the path resolves successfully, click **Start**. The log will display the
selected executable and advance through the steps until the status reads
“Loader ready – click Close to exit.”

## Building a standalone executable

The project can be packaged into a single-file executable using PyInstaller.
From the repository root, run (swapping in `py -3.13` if needed):

```powershell
py -3 -m PyInstaller --noconfirm --onefile --noconsole --name GlandExecutorLoader main.py
# or explicitly
py -3.13 -m PyInstaller --noconfirm --onefile --noconsole --name GlandExecutorLoader main.py
```

The resulting `GlandExecutorLoader.exe` will be available in the `dist/`
directory. Launch the executable to start the GUI without requiring a Python
installation.
