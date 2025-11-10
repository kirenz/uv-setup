# Creating a Project with uv

uv turns Python project setup into a straightforward process. With just a few commands you get a fully configured development environment with the right Python version.

## Create a project with `uv init`

First, create a new project in the command line (Terminal or Git Bash). In this example we use the home directory.

To use a different location, navigate to the desired folder first (e.g. `cd Documents`).

We run `uv init`, specify the project name (`mein-projekt` in this example), and set the Python version (`3.11` here):

```bash
uv init mein-projekt --python 3.11
```

This command creates a new folder named `mein-projekt`.

Change into that directory:

```bash
cd mein-projekt
```

List all files (including hidden ones) with `ls -a`:

```bash
ls -a
```

You should see something like this:

```
mein-projekt/
├── README.md         # Project documentation
├── pyproject.toml    # Project configuration
├── main.py           # Example Python file
├── .python-version   # Required Python version
├── .gitignore        # Git ignore rules
└── .git/             # Git metadata
```

`README.md` provides documentation, `pyproject.toml` contains the project configuration, and `main.py` is a starter example.

A **TOML file** (Tom's Obvious, Minimal Language) is a human-readable configuration format that is still easy for tools to parse. Many projects use TOML when they want clear configuration files.

uv also creates several hidden "dotfiles" that start with a period. They are hidden in normal directory views but provide important functionality.

`.gitignore` controls which files are excluded from version control, and the `.git` directory stores Git metadata. Another hidden file is `.python-version`, which contains the selected Python version.

## Create the virtual environment with `uv sync`

To generate a virtual environment for the project, run `uv sync` (you could also use `uv run`):

```bash
uv sync
```

This creates a `.venv` directory inside the project.

The `.venv` directory contains an isolated Python environment dedicated to your project. uv sets it up with the specified Python version. That means:

- The requested Python version is downloaded and installed automatically
- The environment is ready for installing packages right away
- Other projects remain untouched by the packages you add here

Without an activated virtual environment, packages are installed globally. With the environment activated, packages end up only inside this project.

uv also generates a `uv.lock` file. It is a TOML file managed by uv and should not be edited manually.

The lockfile records every package that was installed. It ensures that team members working on different machines use the same dependency versions.

The lockfile is created and updated whenever you run commands that use the project environment, such as `uv sync` and `uv run`. You can also update it explicitly with `uv lock`.

While `pyproject.toml` defines the project requirements, the lockfile stores the exact package versions installed in the environment. Check it into version control to keep installations reproducible across machines.

To use the virtual environment, activate it first:

```bash
source .venv/bin/activate
```

Check whether Python 3.11 is available. `uv run` ensures the uv-managed environment is used even if you forget to activate it:

```bash
uv run python --version
```

Run the example script to verify everything works:

```bash
uv run python main.py
```

You should see the message "Hello from mein-projekt!".

## Install packages

After the initialization you can start development. Because uv already prepared the environment, you can add packages right away.

In this example we install `pandas` and `openai` with `uv add`:

```bash
uv add pandas openai
```

With every `uv add` command, uv updates both `pyproject.toml` and `uv.lock` and installs the packages into the existing virtual environment.

## uv in VS Code

Open the project in Visual Studio Code (VS Code):

1. Launch VS Code
2. Choose "File" in the menu bar
3. Select "Open Folder..."
4. Pick the `mein-projekt` directory

### Select the Python interpreter

To make VS Code use the correct environment, choose the interpreter from the virtual environment:

- Open the command palette: `Ctrl`+`Shift`+`P` (Windows/Linux) or `Cmd`+`Shift`+`P` (macOS)
- Type "Python: Select Interpreter"
- Pick the interpreter (Python 3.11.xx (mein-projekt)):
  - macOS/Linux: `.venv/bin/python`
  - Windows: `.venv\Scripts\python.exe`
- If it is not listed, use "Enter interpreter path..." and browse to it manually

### Use the integrated terminal

If the terminal panel is not visible yet, open it first.

- Menu: choose "Terminal" -> "New Terminal"

In the terminal panel, move the pointer over the terminal area and click the small **down arrow (`v`)** next to the plus icon (`+`). This opens the list of available terminal profiles.

- Pick **Git Bash** (Windows) or **zsh** (macOS)

A new tab appears in the terminal panel.

Run the example file with uv (this guarantees the project environment is used):

```bash
uv run python main.py
```
