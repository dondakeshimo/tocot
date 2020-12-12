import click


@click.command()
def cmd():
    click.echo("hello")


def main():
    cmd()


if __name__ == "__main__":
    main()
