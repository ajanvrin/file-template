"""Replace the keywords in a file with the contents of another file."""

import click


@click.command()
@click.argument("keyword")
@click.argument(
    "file1", type=click.Path(exists=True, dir_okay=False, allow_dash=True)
)
@click.argument("file2", type=click.File())
@click.option(
    "-i",
    "--inplace",
    is_flag=True,
    help="Edit the file in place instead of outputting to stdout.",
)
@click.option(
    "-n",
    "--no-strip",
    is_flag=True,
    help="Do not strip FILE2 of leading or trailing blank characters.",
)
def main(keyword, file1, file2, inplace=False, no_strip=False):
    """Replace KEYWORD in FILE1 with the contents of FILE2."""
    replacement = file2.read()

    if not no_strip:
        replacement = replacement.strip()

    with open(file1) as template_file:
        template = template_file.read().replace(keyword, replacement)

    if inplace:
        with open(file1, "w") as template_file:
            template_file.write(template)
    else:
        click.echo(template)
