import click
@click.command()
@click.option('--n', default=1, show_default=True)
@click.option("--gr", is_flag=True, show_default=True, default=False, help="Greet the world.")
@click.option("--br", is_flag=True, show_default=True, default=True, help="Add a thematic break")
def dots(n, gr, br):
    if gr:
        click.echo('Hello world!')
    click.echo('.' * n)
    if br:
        click.echo('-' * n)

if __name__ == '__main__':
	dots()
