import argparse
import os.path
import sys
import re
from source.input_checking import check_file_open
import pathlib
from gen_reads_parallel import main

#
#
#
#try validating that the file directory exists (/home/suvinit)
#
def PARSE_1(raw_args=None):
	#Parse Input Arguments
	parser = argparse.ArgumentParser(description = "Operational Flags for NEAT v3.2 subprogram 'gen_reads'", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--r', type=str, required=True, metavar='reference', help="Path to reference fasta")
	parser.add_argument('--R', type=int, required=True, metavar='read_length', help="The desired read length (ideally between 100 and 300)")
	parser.add_argument('--o', type=str, required=True, metavar='output_prefix', help="Use this option to specify where and what to call output files")
	parser.add_argument('--bam', required=False, action='store_true', default=False, help="output golden BAM file")
	args = parser.parse_args(raw_args)
	#Check that reference file is real:
	check_file_open(args.r, 'Error: could not open reference {}'.format(args.r), required=True)
	print("Check 1\n")
	#Write arguments to a cfg file
	try:
		with open('neat.cfg', 'w') as f:
			f.write("Created/overwrote a config file")
			f.write("\n@reference = " + f"{args.r}")
			f.write("\n@read length = " + f"{args.R}")
			f.write("\n@output prefix = " + f"{args.o}")
			f.write("\n@bam = " + f"{args.bam}")
			f.write("\nAnd that's PARSE_1's output\n")
	except FileNotFoundError:
			print("The directory does not exist")
	#print("\n")

def PARSE_2():
	print("Check 2\n")
	output = "/home/suvinit/NEAT/command_script/Gamma"
	pathlib.Path(output)
	print(pathlib.Path(output).parent)
	print(pathlib.Path(output).parent.is_dir())
	if not pathlib.Path(output).parent.is_dir():
		pathlib.Path(output).parent.mkdir()
		print(pathlib.Path(output).parent.is_dir())
	print(pathlib.Path(output).parent)
	#
#
if __name__ == '__main__':
	print("\nThe pacer fitness test starts now:\n")
	PARSE_1()
	print("\nBah-weep-Graaaaagnah weep ni ni bong\n")
	PARSE_2()
################################<THOUGHTS BELOW>################################
'''
When opening config.txt in write-mode
Realized that the config file only opens in same directory as script
Maybe change that?
clear && python3 kappa.py --r /home/suvinit/NEAT-data/ --R 100 --o /home/suvinit/NEAT/command_script && ls && cat neat.cfg
'''

#In progress...
