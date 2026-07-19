from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def show_banner():
    banner = Text("""
██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║╚██╗██╔╝
██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║ ╚███╔╝
██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║ ██╔██╗
██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║██╔╝ ██╗
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
""", style="bold cyan")

    console.print(
        Panel(
            banner,
            title="[bold green]ReconX[/bold green]",
            subtitle="Automated Reconnaissance Framework",
            border_style="cyan",
        )
    )

    console.print("[bold yellow]Version:[/bold yellow] 1.0")
    console.print("[bold yellow]Author:[/bold yellow] John Paul\n")
