#################################################################################################################
   #FROM https://click.palletsprojects.com/en/8.1.x/
   import click

   @click.command()
   %click inline

   @click.option('--count', default=1, help='Number of greetings.')
   @click.option('--name', prompt='Your name',
      help='The person to greet.')
   def hello(count, name):
      """Simple program that greets NAME for a total of COUNT times."""
      for x in range(count):
         click.echo(f"Hello {name}!")

   if __name__ == '__main__':
      hello()
#################################################################################################################
#getopts method

#python

import sys
import click
@click.command()

def welcome_statement():
    click.echo("Welcome to the NEAT project, the NExt-generation sequencing Analysis Toolkit, version 3.2.")

def main(argv):
   read_length = ''
   reference_fasta_file = ''
   output_file = ''

   #1>>redo options with click.option
   try:
      opts, args = getopt.getopt(argv,"R:r:o:",["read_length=","reference_fasta=", "output="])
   except getopt.GetoptError:
      print('test.py -R <read_length> -r <reference_fasta> -o <output_file>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-R", "--read_length"):
         read_length = arg
      elif opt in ("-r", "--reference_fasta"):
         reference_fasta_file = arg
      elif opt in ("-o", "--output"):
         output_file = arg

      print('read_length is:  "', read_length)
      print('reference_fasta is "', reference_fasta_file)
      print('Output is "', output_file)

   return read_length
   return reference_fasta_file
   return output_file

if __name__ == "__main__":
     main(sys.argv[1:])
#################################################################################################################
#1>>redo options with click.option
import click
@click.command()
@click.option('--r', prompt = /home/suvinit/NEAT-data/H1N1/H1N1.fasta, help = 'Path to reference fasta')
@click.option('--R', default = 100, help = 'The desired read length')
@click.option('--o', default = /home/suvinit/NEAT-data/H1N1/H1N1.test-run, help = 'output_prefix')

#def hello(count, name):
#   """Simple program that greets NAME for a total of COUNT times."""
#   for x in range(count):
#      click.echo(f"Hello {name}!")

#if __name__ == '__main__':
#   hello()
#################################################################################################################
python3 ......./gen_reads.py -r 101 -R /...../rando.fa -o ...../testpiece.fa
#################################################################################################################
