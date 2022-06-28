import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
#this does not work, use --count <#> instead:
#@click.option('--count', prompt='How many times?', help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
#this does work:
#@click.option('--name', default='Josh', help='The person to greet.')


#    """Simple program that greets NAME for a total of COUNT times."""
#    for x in range(count):
#        click.echo(f"Hello {name}!")
#if __name__ == '__main__':
#    hello()
#        click.echo(f"Hello {name}!")
