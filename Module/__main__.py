import click


@click.command("hello")
def hello():
    click.echo("Hello, World!")


if __name__ == "__main__":
    hello()
