import click
import os.path
@click.command()
#@click.option('--file_path', required=True, show_default=True, help='Path to reference fasta', type=click.Path(exists=True))
@click.option('--file_path', required=True, show_default=True, default = "/home/suvinit/NEAT-data/H1N1/H1N1.fa", help='Path to reference fasta', type=click.Path(exists=True))
#find a fix for capitalization
@click.option('--read_length', required=True, default=100, show_default=True, help='The desired read length') #try to test is < this is within a certain range (50,300)
@click.option('--output_path', default="/home/suvinit/NEAT/testing_command_script/H1N1.test-run", show_default=True, help='output_prefix')
@click.option('--bam', default=False, is_flag=True, show_default=True, help='output golden BAM file')
#try validating that the file directory exists (/home/suvinit)
def gen_config_file(file_path, read_length, output_path, bam):
	click.echo(f'\nHello, the input path the a reference fasta is: {file_path}' + f'\nHello, the read length is: {read_length}' + f'\nHello, the output path is: {output_path}')
	click.echo("\nCongrats Varenya! This code actually compiles!")
	click.echo("(with a --file_path followed by an actual filepath, like /home/suvinit/NEAT-data/H1N1/H1N1.fa)")
	try:
		with open('neat.cfg', 'w') as f:
			f.write("Created/overwrote a config file")
			r = file_path
			R = read_length
			o = output_path
			f.write("\n@r = " + f"{r}")
			f.write("\n@R = " + f"{R}")
			f.write("\n@o = " + f"{o}")
			f.write("\n@bam = " + f"{bam}")
			f.write("\n")
	except FileNotFoundError:
			print("The directory does not exist")
	print("\nHi Josh!")
	print("<hello> is done")

#combine code from readingBETA
def read_back_cfg():
	print("Check 2.1")
	try:
		mylines = []
		with open ('neat.cfg', "rt") as myfile:
			for line in myfile:
				mylines.append(line)
			print("\nCheck 2.2\n")
			for element in mylines:
				if "@" in mylines:
				    element=mylines[mylines.find("@")+1:].split()[0]
				else:
				    element=element
				print(element)
				print("\nCheck 2.3\n")
			print("\nCheck 2.4\n")
			myfile.seek(0)
			for line in myfile:
				print(mylines[0].find(" = "))
			print("\nCheck 2.5\n")
			myfile.seek(0)
			print(myfile.readlines())
			print("\nCheck 2.6\n")
			myfile.seek(0)
			count = 0
			while True:
				count += 1
				line = myfile.readline()
				if not line:
					break
				print("Line{}: {}".format(count, line.strip()))
			print("\nCheck 2.7\n")
	except FileNotFoundError:
            print("There is a FileNotFoundError\n")
            print("\nHi Josh!")

if __name__ == '__main__':
	print("\nLet's get this party started\n")
	gen_config_file()
	print("\nThis is where the fun begins\n")
	read_back_cfg()
	print("\nBah-weep-Graaaaagnah weep ni ni bong\n")
################################<THOUGHTS BELOW>################################
#When opening config.txt in write-mode
#Realized that the config file only opens in same directory as script
#Maybe change that?
#In progress...
