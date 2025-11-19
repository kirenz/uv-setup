# Installing uv

[uv](https://docs.astral.sh/uv/) is a package and project manager for Python. It combines installation, virtual environments, and dependency management in a single tool.

> [!NOTE]
> On Windows I recommend using [Git Bash](https://git-scm.com/download/win) to install and use uv. 

1. Open Terminal (macOS) or Git Bash (Windows)

2. Run the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

3. Close the current terminal window.

4. Open a new Terminal or Git Bash window.

5. Confirm that uv is available:

```bash
uv --version
```

You should see a version number (e.g. `0.9.10`).


> [!TIP]
If the installation failed, try the steps outlined in Troubleshooting.

## Troubleshooting

**Windows**

Use PowerShell instead of Git Bash and use the following command:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS**

Install the package manager [Homebrew](https://brew.sh/) first (if not installed yet):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install uv with:

```bash
brew install uv
```

If you get "Permission denied" errors, follow the steps here:

- [Fix permission errors on macOS](permission-mac.md)
