import click
 
@click.command()
@click.argument("greeting")
def cli(greeting):
    '''
    This is the default CLI method.
 
    Arguments:
            greeting: {string}
    '''
 
    click.echo(greeting)
    click.echo ("This is a simple cli.")
 
if __name__=="__main":
    cli()
