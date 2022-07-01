import test_command
#from test_command import file_path
#from test_command import read_length
#from test_command import output_path

#from test_command import file_path, read_length, output_path

#import click
#@click.command()
#@click.option('--file_path', required=True, show_default=True, help='Path to reference fasta', type=click.Path(exists=True))
#@click.option('--read_length', required=True, default=100, show_default=True, help='The desired read length') #try to test is < this is within a certain range (50,300)
#@click.option('--output_path', default="/home/suvinit/NEAT/testing_command_script/H1N1.test-run", show_default=True, help='output_prefix')
#@click.option('--bam', default=False, is_flag=True, show_default=True, help='output golden BAM file')
def HelloThereGeneralKenobi():
    try:
        with open('config.txt', 'r') as f:
            print("Does this work? #1\n")
            print("The config file contains the following:\n")
            #to print out the array of all lines with brackets, use:
            print("\nreadlines makes:\n")
            print(f.readlines())
            f.seek(0)
            #to print out every line use:
            print("\nreadline makes:\n")
            print(f.readline())
            f.seek(0)
            print("read makes:\n")
            print(f.read())
            f.seek(0)
            print("And that's all folks!")
            print()
            f.seek(0)

            r = file_path
            R = read_length
            o = output_path
            print('the value of r is %s\n' % str(r))
            print('the value of R is %s\n' % int(R))
            print('the value of o is %s\n' % str(o))
            #

    except FileNotFoundError:
            print("There is a FileNotFoundError\n")
    print("\nHi Josh!")

if __name__ == '__main__':
	HelloThereGeneralKenobi()
################################<TASK BELOW>################################
#Still working on importing variables from test_command.property
#<python3 readingALPHA.py> still prints this to the terminal:
'''
    Does this work? #1

The config file contains the following:

readlines makes:

['Created/overwrote a config file\n', '@r = /home/suvinit/NEAT-data/H1N1/H1N1.fa\n', '@R = 250\n', '@o = /home/suvinit/Desktop/\n', '@bam = False\n']
readline makes:

Created/overwrote a config file

read makes:

Created/overwrote a config file
@r = /home/suvinit/NEAT-data/H1N1/H1N1.fa
@R = 250
@o = /home/suvinit/Desktop/
@bam = False

And that's all folks!

Traceback (most recent call last):
  File "readingALPHA.py", line 47, in <module>
    HelloThereGeneralKenobi()
  File "readingALPHA.py", line 34, in HelloThereGeneralKenobi
    r = file_path
NameError: name 'file_path' is not defined
'''
