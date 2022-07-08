"""
Command line interface for NEAT's generate reads function, with
"""

import argparse

from ...read_simulator import read_simulator_runner
from .base import BaseCommand
from .options import output_group
import yaml


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
        parser.add_argument('-r', type=str, dest = 'Reference File', required=True, metavar='reference', help="Path to reference fasta")
        parser.add_argument('-R', type=int, dest = 'Read Length', required=True, metavar='read_length', help="The desired read length (ideally between 100 and 300)")
        parser.add_argument('--bam', dest = 'Bam Output', required=False, action='store_true', default=False, help="output golden BAM file")
        parser.add_argument('-c', type=float, dest = 'Average Coverage', required=False, metavar='coverage', default=10.0, help="Average coverage, default is 10.0")
        parser.add_argument('-e', type=str, dest = 'Error Model', required=False, metavar='error_model', default=None, help="Location of the file for the sequencing error model (omit to use the default)")
        parser.add_argument('-E', type=float, dest = 'Error Rate', required=False, metavar='Error rate', default=-1, help="Rescale avg sequencing error rate to this, must be between 0.0 and 0.3")
        parser.add_argument('-p', type=int, dest = 'Desired Ploidy', required=False, metavar='ploidy', default=2, help="Desired ploidy, default = 2")
        parser.add_argument('-tr', type=str, dest = 'Target Region File', required=False, metavar='target.bed', default=None, help="Bed file containing targeted regions")
        parser.add_argument('-dr', type=str, dest = 'Discard Region File', required=False, metavar='discard_regions.bed', default=None, help="Bed file with regions to discard")
        parser.add_argument('-to', type=float, dest = 'Off Target Coverage Scalar', required=False, metavar='off-target coverage scalar', default=0.00, help="off-target coverage scalar")
        parser.add_argument('-m', type=str, dest = 'Mutation Model File', required=False, metavar='model.p', default=None, help="Mutation model pickle file")
        parser.add_argument('-M', type=float, dest = 'Mutation Rescale Rate', required=False, metavar='avg mut rate', default=-1, help="Rescale avg mutation rate to this (1/bp), must be between 0 and 0.3")
        parser.add_argument('-Mb', type=str, dest = 'Positional Mutation File', required=False, metavar='mut_rates.bed', default=None, help="Bed file containing positional mut rates")
        parser.add_argument('-N', type=int, dest = 'Minimum Quality Score', required=False, metavar='min qual score', default=-1, help="below this quality score, replace base-calls with N's")
        parser.add_argument('-v', type=str, dest = 'Variant Input', required=False, metavar='vcf.file', default=None, help="Input VCF file of variants to include")

        parser.add_argument('--pe', nargs=2, type=int, dest = 'Paired End Values', required=False, metavar=('<int>', '<int>'), default=(None, None), help='Paired-end fragment length mean and std')
        parser.add_argument('--pe-model', type=str, required=False, metavar='<str>', default=None, help='empirical fragment length distribution')
        parser.add_argument('--gc-model', type=str, required=False, metavar='<str>', default=None, help='empirical GC coverage bias distribution')
        parser.add_argument('--vcf', dest = 'VCF Output', required=False, action='store_true', default=False, help='output golden VCF file')
        parser.add_argument('--fa', dest = 'Fasta vs Fastq', required=False, action='store_true', default=False, help='output FASTA instead of FASTQ')
        parser.add_argument('--rng', type=int, dest = 'RNG Seed Value', required=False, metavar='<int>', default=-1, help='rng seed value; identical RNG value should produce identical runs of the program, so things like read locations, variant positions, error positions, etc, should all be the same.')
        parser.add_argument('--no-fastq', required=False, action='store_true', default=False, help='bypass fastq generation')
        parser.add_argument('--discard-offtarget', required=False, action='store_true', default=False, help='discard reads outside of targeted regions')
        parser.add_argument('--force-coverage', required=False, action='store_true', default=False, help='[debug] ignore fancy models, force coverage to be constant')
        parser.add_argument('--rescale-qual', required=False, action='store_true', default=False, help='Rescale quality scores to match -E input')
        parser.add_argument('-d', dest = 'Debug Mode Activation Status', required=False, action='store_true', default=False, help='Activate Debug Mode')
        #

        output_group.add_to_parser(parser)

    def execute(self, arguments: argparse.Namespace):
        """
        Execute the command.

        :param arguments: The namespace with arguments and their values.
        """
        args_dict = arguments.__dict__
        my_dict = {}
        for key in args_dict.keys():
            my_dict[key] = args_dict[key]
        #

        with open('neat.cfg', 'w') as file:
            documents = yaml.dump(my_dict, file)


        #read_simulator_runner(arguments.config, arguments.output)
        read_simulator_runner("neat.cfg", arguments.output)
