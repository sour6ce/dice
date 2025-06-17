import typer
import random
from typing import List

app = typer.Typer()


def chunk_list(lst: List[str], chunk_size: int) -> List[List[str]]:
    """Split a list into chunks of specified size."""
    return [lst[i : i + chunk_size] for i in range(0, len(lst), chunk_size)]


@app.command()
def random_choice(
    items: list[str] = typer.Argument(help="List of items to choose from"),
    num_choices: int = typer.Option(1, "--num", "-n", help="Number of items to choose"),
    group_size: int = typer.Option(
        1, "--group", "-g", help="Number of items per group"
    ),
):
    """Print random items from the given list, optionally grouped."""
    if not items:
        typer.echo("Please provide at least one item")
        raise typer.Exit(code=1)

    if num_choices < 1:
        typer.echo("Number of choices must be at least 1")
        raise typer.Exit(code=1)

    if group_size < 1:
        typer.echo("Group size must be at least 1")
        raise typer.Exit(code=1)

    if num_choices > len(items):
        typer.echo(
            f"Warning: Requested {num_choices} choices but only {len(items)} items available"
        )
        num_choices = len(items)

    chosen = random.sample(items, num_choices)
    groups = chunk_list(chosen, group_size)

    for i, group in enumerate(groups, 1):
        if len(groups) > 1:
            typer.echo(f"({i}):")
        for item in group:
            typer.echo(f"{item}")
        if i < len(groups):
            typer.echo()  # Add blank line between groups


if __name__ == "__main__":
    app()
