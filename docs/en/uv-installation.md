# Installing uv

1. Open Terminal (macOS) or Git Bash (Windows)
2. Run the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If `curl` is not available, you can use `wget` instead:

```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

3. Wait until the installation finishes

After the installation you should confirm that uv is available:

4. Close the current terminal window.
5. Open a new Terminal or Git Bash window
6. Enter the command:

```bash
uv --version
```

You should see a version number (e.g. `0.6.8`)

Try the steps outlined in Troubleshooting if the installation fails.

## Troubleshooting

### Windows

Use PowerShell instead of Git Bash and use the following command:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### macOS

Install the package manager Homebrew first (if not installed yet):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then install uv with:

```bash
brew install uv
```

If you get "Permission denied" errors, follow the steps in the guide below:

- [Fix permission errors on macOS](permission-mac.md)
