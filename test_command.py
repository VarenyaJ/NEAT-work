#1>>redo options with click.option
import click
@click.command()
@click.option('--r', prompt = "/home/suvinit/NEAT-data/H1N1/H1N1.fasta", help = 'Path to reference fasta')
@click.option('--R', default = 100, help = 'The desired read length')
@click.option('--o', default = "/home/suvinit/NEAT-data/H1N1/H1N1.test-run", help = 'output_prefix')

if __name__ == '__main__':
	hello()

#def hello(count, name):
#   """Simple program that greets NAME for a total of COUNT times."""
#   for x in range(count):
#      click.echo(f"Hello {name}!")

#if __name__ == '__main__':
#   hello()
