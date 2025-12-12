from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import emoji

def main():
    console = Console()

    # 1. Use 'emoji' to create icons
    rocket = emoji.emojize(":rocket:")
    check = emoji.emojize(":check_mark_button:")
    fire = emoji.emojize(":fire:")

    # 2. Use 'rich' to create a table
    table = Table(title="uv Setup Status")

    table.add_column("Package", style="cyan", no_wrap=True)
    table.add_column("Installed", justify="center")
    table.add_column("Role", style="magenta")

    table.add_row("rich", f"[green]{check}[/green]", "UI & Formatting")
    table.add_row("emoji", f"[green]{check}[/green]", "Icons & Fun")
    table.add_row("uv", f"[green]{check}[/green]", f"Speed {rocket}")

    # 3. Print the output
    console.print(Panel(f"[bold yellow]Hello from uv-setup![/bold yellow] {fire}", expand=False))
    console.print(table)
    console.print("\n[dim]Success! Your environment is ready.[/dim]")

if __name__ == "__main__":
    main()