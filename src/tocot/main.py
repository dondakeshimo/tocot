import typing

import click


def validate_level(ctx, param, value):
    level = value

    if level <= 0:
        raise click.BadParameter("level must be greater than 0.")
    if level > 5:
        raise click.BadParameter("level must be less than 6")


@click.command()
@click.argument("in_file", type=click.File("r"))
@click.argument("out_file", type=click.File("w"))
@click.option("-l", "--level", callback=validate_level, default=2, type=int)
def cmd(in_file: typing.TextIO, out_file: typing.TextIO) -> None:
    click.echo(input.read(100))


def main():
    cmd()


if __name__ == "__main__":
    main()
