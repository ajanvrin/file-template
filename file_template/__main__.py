"""Replaces the keywords in a file with the contents of another file.
"""

from importlib import resources

import click
import icecream

with resources.path("file_template", "banner.txt") as banner_path:
    with open(banner_path) as f:
        BANNER = f.read()


@click.command()
@click.argument("keyword")
@click.argument("file1", type=click.Path())
@click.argument("file2", type=click.File("r"))
def main(keyword, file1, file2):
    """Replaces KEYWORD in FILE1 withthe contents of FILE2."""
    
    click.echo(BANNER, err=True)

    with open(file1) as f:
        template = f.read()

    with open(file1, "w") as f:
        f.write(template.replace(keyword, file2.read()))
