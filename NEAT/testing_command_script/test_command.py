import click
@click.command()
#no capital letters:
@click.option('--file_path', default = "/home/suvinit/NEAT-data/H1N1/H1N1.fa", show_default=True, help = 'Path to reference fasta', type=click.Path(exists=True))

@click.option('--read_length', default = 100, show_default=True, help = 'The desired read length')
#try to test is ^ this is within a certain range (50,300)

@click.option('--output_path', default = "/home/suvinit/NEAT-data/H1N1/H1N1.test-run", show_default=True, help = 'output_prefix')
@click.option('--bam', default=False, is_flag=True, show_default=True, help='output golden BAM file')
###
@click.option('--n', default=1, show_default=True)
@click.option("--gr", is_flag=True, show_default=True, default=False, help="Greet the world.")
@click.option("--br", is_flag=True, show_default=True, default=True, help="Add a thematic break")
################################<TASK BELOW>################################
#try validating that the file directory exists (/home/suvinit)
def hello(file_path, read_length, output_path, bam, n, gr, br):
	click.echo(f'Hello {file_path}' + f'\nHello {read_length}' + f'\nHello {output_path}')
	click.echo(f'\noutput bam test line:\n {bam}')
	###
	if gr:
		click.echo('Hello world!')
		click.echo('\n')
		click.echo('.' * n)
	if br:
		click.echo('\n')
		click.echo('-' * n)

if __name__ == '__main__':
	hello()

################################<TASK BELOW>################################
#create config file
#append with only user inputs
#if input DNE then exit with error
#test with file_path, if none then error exit
#?
#	dynamic defaults for prompts?
#	single option boolean flags?
