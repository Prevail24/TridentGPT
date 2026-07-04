from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.config import Config

console = Console()


class MissionRenderer:
    def render(self, mission):
        console.print()

        console.print(
            Panel.fit(
                f"[bold cyan]⚓ {mission.title}[/bold cyan]\n"
                "[italic]Mission Intelligence[/italic]",
                border_style="cyan",
            )
        )

        table = Table(show_header=False, box=None)

        table.add_row("[bold]Mission ID[/bold]", mission.id)
        table.add_row("[bold]Status[/bold]", mission.status.upper())
        table.add_row("[bold]Priority[/bold]", mission.priority.upper())
        table.add_row("[bold]Observer[/bold]", mission.observer)

        console.print(table)
        console.print()

        console.rule("[cyan]Observation Threads")

        if mission.observations:
            for observation_id in mission.observations:
                console.print(f"[green]✓[/green] {observation_id}")
        else:
            console.print("[yellow]No observations yet.[/yellow]")

        console.print()
        console.print(f"[italic dim]{Config.BRAND_QUOTE}[/italic dim]")