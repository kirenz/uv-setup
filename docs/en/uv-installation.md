# Installing uv
[Deutsch](../de/uv-installation.md) | English

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

## Verify the installation

After the installation you should confirm that uv is available:

1. Open a new Terminal or Git Bash window
2. Enter the command:

```bash
uv --version
```

3. You should see a version number (e.g. `0.6.8`)

## Troubleshooting

If the command `uv --version` is not found, it may be due to permission issues. In that case, consult the guide for fixing "Permission denied" errors:

- [Fix permission errors on macOS](permission-mac.md)
