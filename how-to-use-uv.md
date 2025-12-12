# How to use uv?

![uv](https://img.shields.io/badge/uv-managed-430f8e.svg?style=flat&logo=python&logoColor=white)

>**uv** is a modern tool that helps you manage Python projects. Think of it as an all-in-one assistant that takes care of the technical setup so you can focus on writing code.

## Table of Contents

- [Why Do You Need It?](#why-do-you-need-it)
- [Your Typical Workflow](#your-typical-workflow)
- [Working with Existing Projects from GitHub](#working-with-existing-projects-from-github)
- [Project Files uv Creates](#project-files-uv-creates)
- [Keeping uv Up to Date](#keeping-uv-up-to-date)

## Why Do You Need It?

When working with Python, you typically need to:

- Install Python itself
- Keep track of which external libraries (packages) your project uses
- Make sure different projects don't interfere with each other
- Share your project with others so they can run it too

**uv does all of this for you automatically.**

## Your Typical Workflow

Here's how you'll use uv to create and work on a new project:

### Step 1: Open Your Terminal

Open the comand line interace (like Terminal or Git Bash) on your computer.

### Step 2: Navigate to Your Projects Folder

Go to the folder where you want to create your project. For example:

```bash
cd my-python-projects
```

### Step 3: Create a New Project

Create a new project with this command:

```bash
uv init my-project --python 3.12
```

**What each part means:**
- `uv init` = tells uv to create a new project
- `my-project` = the name of your project (you can change this)
- `--python 3.12` = specifies which Python version to use

### Step 4: Enter Your Project Folder

Move into your newly created project folder:

```bash
cd my-project
```

### Step 5: Add Python Packages

Add any external libraries your project needs. For example, to add rich (makes terminal text colorful and formatted):

```bash
uv add rich
```

You can also add multiple packages as needed:

```bash
uv add rich emoji
```

### Step 6: Open in Your Code Editor

Open the project in VS Code (or your preferred editor).



### Step 7: Run Your Code

In VS Code's integrated terminal, run your Python scripts:

```bash
uv run main.py
```

>[!IMPORTANT]
Make sure to use the integrated terminal where you installed uv (e.g., Git Bash for Windows).


**What this does:**
- `uv run` = tells uv to run a command using your project's Python environment


uv looks at the file extension (.py), realizes it is a Python script, and automatically invokes the Python interpreter for you.


## Working with Existing Projects from GitHub

Sometimes you'll need to work on a project that already exists (for example, a project on GitHub which uses uv). 

Here's what to do (we'll use this repo as an example):

### Step 1: Clone the Project

First, clone the repository from GitHub:

```bash
git clone https://github.com/kirenz/uv-setup
```

### Step 2: Navigate into the Project

Move into the project folder:

```bash
cd uv-setup
```

### Step 3: Sync Dependencies with `uv sync`

This is the important step! Use `uv sync` to install all the packages the project needs:

```bash
uv sync
```

**What `uv sync` does:**
- Reads the `pyproject.toml` and `uv.lock` files
- Installs the exact same packages and versions that the project requires
- Sets up the isolated environment (`.venv` folder)
- Ensures your setup matches everyone else's

### Step 4: Open and Run

Now you can open the project in VS Code and work normally:

Run the code:

```bash
uv run main.py
```



## Project Files uv Creates

When you create a project, uv automatically generates several important files:

### `pyproject.toml`
This is your project's main configuration file. It contains:
- Your project's name
- The Python version you're using
- A list of all packages your project needs

### `uv.lock`
A detailed record of the exact versions of all packages installed. This ensures everyone working on the project uses the same versions.

### `.python-version`
Specifies which Python version your project uses (in this case, 3.12).

### `.venv/` folder
A hidden folder containing your project's isolated Python environment. You don't need to touch this folder - uv manages it automatically. This keeps your project's packages separate from other projects.

### `main.py`
A starter Python file where you can begin writing your code.

## Keeping uv Up to Date

It's a good idea to occasionally update uv to get the latest features and bug fixes.

### Check Your Current Version

To see which version of uv you have installed:

```bash
uv --version
```

### Update uv

To update uv to the latest version:

```bash
uv self update
```

<details>
<summary> Click here if you get an error </summary>

<br>
If uv self update gives you an error saying it is disabled or not managed by uv, use the command matching your package manager. For example:


**For pip installations:**

```bash 
pip install --upgrade uv
```

**For macOS with Homebrew:**

```bash 
brew upgrade uv
```

</details>

**Why update?**
- Get new features and improvements
- Fix bugs and security issues
- Ensure compatibility with the latest Python packages

You don't need to update constantly - maybe once every few months or when you encounter issues.

## The Bottom Line

uv simplifies Python project management so you can spend less time on setup and more time learning and building. Follow the workflow above, and uv handles all the technical details automatically.
