"""Replaces the keywords in a file with the contents of another file."""

from importlib import resources

import click

with resources.path("file_template", "banner.txt") as banner_path:
    with open(banner_path) as f:
        BANNER = f.read()


@click.command()
@click.argument("keyword")
@click.argument("file1", type=click.File())
@click.argument("file2", type=click.File())
def main(keyword, file1, file2):
    """Replaces KEYWORD in FILE1 with the contents of FILE2."""
    click.echo(BANNER, err=True)

    template = file1.read()

    click.echo(template.replace(keyword, file2.read()))
