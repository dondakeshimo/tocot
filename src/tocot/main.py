import typing

import click

from .toc_builder import TOCBuilder


def validate_level(ctx, param, value):
    level = value

    if level <= 0:
        raise click.BadParameter("level must be greater than 0.")
    if level > 5:
        raise click.BadParameter("level must be less than 6")

    return level


@click.command()
@click.argument("in_file", type=click.File("r"))
@click.argument("out_file", type=click.File("w"))
@click.option("--level", "-l", callback=validate_level, default=2,
              show_default=True, type=int)
def cmd(in_file: typing.TextIO, out_file: typing.TextIO, level: int) -> None:
    builder = TOCBuilder(in_file, out_file, level)
    builder.build()
    builder.write()


def main():
    cmd()


if __name__ == "__main__":
    main()
