"""
Command line interface for NEAT's generate reads function, with
"""

import argparse

#attempted relative import with no known parent package
#from ...read_simulator import read_simulator_runner
import sys
sys.path.insert(0, '/home/suvinit/NEAT/neat/read_simulator')
from runner import read_simulator_runner

from .base import BaseCommand
from .options import output_group

#imports from command_script>epsilon.py
import os
from input_checking import check_file_open
import pathlib
import gen_reads_parallel
from gen_reads_parallel import *


class Command(BaseCommand):
    """
    Class that generates a Dataset of simulated NGS reads. NEAT first generates a set of variants to insert, then
        generates fragments to sample from and adds sampling errors to the reads.

    Optional outputs include a golden vcf showing all inserted true variants (i.e., not the simulated errors),
        a golden BAM showing a fast alignment against the region where the read came from,
        a fasta file containing the inserted variants only (no errors).
    """

    name = "read_simulator_cli"
    description = "Simulate NGS reads dataset (See README for complete description of the config input)."

    def add_arguments(self, parser: argparse.ArgumentParser):
        """
        Add the command's arguments to its parser

        :param parser: The parser to add arguments to.
        """
        parser = argparse.ArgumentParser(description = "Operational Flags for NEAT v3.2 subprogram 'gen_reads'", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('--r', type=str, required=True, metavar='reference', help="Path to reference fasta")
        parser.add_argument('--R', type=int, required=True, metavar='read_length', help="The desired read length (ideally between 100 and 300)")
        parser.add_argument('--o', type=str, required=True, metavar='output_prefix', help="Use this option to specify where and what to call output files")
        parser.add_argument('--bam', required=False, action='store_true', default=False, help="output golden BAM file")
        #06.24.2022: Bring in all the other original flags from GR
        parser.add_argument('-c', type=float, required=False, metavar='coverage', default=10.0, help="Average coverage, default is 10.0")
        parser.add_argument('-e', type=str, required=False, metavar='error_model', default=None, help="Location of the file for the sequencing error model (omit to use the default)")
        parser.add_argument('-E', type=float, required=False, metavar='Error rate', default=-1, help="Rescale avg sequencing error rate to this, must be between 0.0 and 0.3")
        parser.add_argument('-p', type=int, required=False, metavar='ploidy', default=2, help="Desired ploidy, default = 2")
        parser.add_argument('-tr', type=str, required=False, metavar='target.bed', default=None, help="Bed file containing targeted regions")
        parser.add_argument('-dr', type=str, required=False, metavar='discard_regions.bed', default=None, help="Bed file with regions to discard")
        parser.add_argument('-to', type=float, required=False, metavar='off-target coverage scalar', default=0.00, help="off-target coverage scalar")
        parser.add_argument('-m', type=str, required=False, metavar='model.p', default=None, help="Mutation model pickle file")
        parser.add_argument('-M', type=float, required=False, metavar='avg mut rate', default=-1, help="Rescale avg mutation rate to this (1/bp), must be between 0 and 0.3")
        parser.add_argument('-Mb', type=str, required=False, metavar='mut_rates.bed', default=None, help="Bed file containing positional mut rates")
        parser.add_argument('-N', type=int, required=False, metavar='min qual score', default=-1, help="below this quality score, replace base-calls with N's")
        parser.add_argument('-v', type=str, required=False, metavar='vcf.file', default=None, help="Input VCF file of variants to include")
        parser.add_argument('--pe', nargs=2, type=int, required=False, metavar=('<int>', '<int>'), default=(None, None), help='Paired-end fragment length mean and std')
        #parser.add_argument('--pe-model', type=str, required=False, metavar='<str>', default=None, help='empirical fragment length distribution')
        #parser.add_argument('--gc-model', type=str, required=False, metavar='<str>', default=None, help='empirical GC coverage bias distribution')
        parser.add_argument('--vcf', required=False, action='store_true', default=False, help='output golden VCF file')
        parser.add_argument('--fa', required=False, action='store_true', default=False, help='output FASTA instead of FASTQ')
        parser.add_argument('--rng', type=int, required=False, metavar='<int>', default=-1, help='rng seed value; identical RNG value should produce identical runs of the program, so things like read locations, variant positions, error positions, etc, should all be the same.')
        parser.add_argument('-d', required=False, action='store_true', default=False, help='Activate Debug Mode')
        #parser.add_argument('--no-fastq', required=False, action='store_true', default=False, help='bypass fastq generation')
        #parser.add_argument('--discard-offtarget', required=False, action='store_true', default=False, help='discard reads outside of targeted regions')
        #parser.add_argument('--force-coverage', required=False, action='store_true', default=False, help='[debug] ignore fancy models, force coverage to be constant')
        #parser.add_argument('--rescale-qual', required=False, action='store_true', default=False, help='Rescale quality scores to match -E input')
        args = parser.parse_args(raw_args)
        #Check that reference file is real:
        check_file_open(args.r, 'Error: could not open reference {}'.format(args.r), required=True)
        print("Check 1\n")
        r = args.r
        R = args.R
        o = args.o
        print("r is " + f"{r}" + "\n")
        print("R is " + f"{R}" + "\n")
        print("o is " + f"{o}" + "\n")
        #Write arguments to a cfg file
        try:
            with open('neat.cfg', 'w') as f:
                f.write("#Created/overwrote a config file")
                f.write("\n@reference = " + f"{args.r}")
                f.write("\n@read_len = " + f"{args.R}")
                f.write("\n@output prefix = " + f"{args.o}")
                f.write("\n@bam = " + f"{args.bam}")
                f.write("\n@coverage = " + f"{args.c}")
                f.write("\n@error_model = " + f"{args.e}")
                f.write("\n@Error rate = " + f"{args.E}")
                f.write("\n@ploidy = " + f"{args.p}")
                f.write("\n@target.bed = " + f"{args.tr}")
                f.write("\n@discard_regions.bed = " + f"{args.dr}")
                f.write("\n@off-target coverage scalar = " + f"{args.to}")
                f.write("\n@model.p = " + f"{args.m}")
                f.write("\n@avg mut rate = " + f"{args.M}")
                f.write("\n@mut_rates.bed = " + f"{args.Mb}")
                f.write("\n@min qual score = " + f"{args.N}")
                f.write("\n@vcf.file = " + f"{args.v}")
                f.write("\n@Paired-end mode = " + f"{args.pe}")
                #f.write("\n@Empirical Fragment Length Distribution = " + f"{args.pe-model}")
                #f.write("\n@Empirical GC Coverage Bias Distribution = " + f"{args.gc-model}")
                f.write("\n@vcf = " + f"{args.vcf}")
                f.write("\n@fasta = " + f"{args.fa}")
                f.write("\n@RNG Seed Value = " + f"{args.rng}")
                f.write("\n@Activate Debug Mode = " + f"{args.d}")
                '''
                f.write("\n@Bypass FastQ Gen = " + f"{args.no-fastq}")
                f.write("\n@Discard Outside Target Reads = " + f"{args.discard-offtarget}")
                f.write("\n@Force Coverage = " + f"{args.force-coverage}")
                f.write("\n@Rescale quality scores to match -E input = " + f"{args.rescale-qual}")
                '''
                f.write("\n#And that's PARSE_1's output\n")
        except FileNotFoundError:
                print("The directory does not exist")
        print("Check 1.1\n")
        return(o)



        output_group.add_to_parser(parser)

    def execute(self, arguments: argparse.Namespace):
        """
        Execute the command.

        :param arguments: The namespace with arguments and their values.
        """

        read_simulator_runner(arguments.config, arguments.output)
