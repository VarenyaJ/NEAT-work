# The NEAT Project v3.2
Welcome to the NEAT project, the NExt-generation sequencing Analysis Toolkit, version 3.2. Neat has now been updated with Python 3, and is moving toward PEP8 standards. There is still lots of work to be done. See the [ChangeLog](ChangeLog.md) for notes.

Stay tuned over the coming weeks for exciting updates to NEAT, and learn how to [contribute](CONTRIBUTING.md) yourself. If you'd like to use some of our code, no problem! Just review the [license](LICENSE.md), first.

NEAT-gen_reads is a fine-grained read simulator. GenReads simulates real-looking data using models learned from specific datasets. There are several supporting utilities for generating models used for simulation.

This is an in-progress v3.2 of the software. For a stable release of the previous repo, please see: [genReads1](https://github.com/zstephens/genReads1) (or check out our v2.0 tag)

To cite this work, please use:

> Stephens, Zachary D., Matthew E. Hudson, Liudmila S. Mainzer, Morgan Taschuk, Matthew R. Weber, and Ravishankar K. Iyer. "Simulating next-generation sequencing datasets from empirical mutation and sequencing models." PloS one 11, no. 11 (2016): e0167047.


Table of Contents
=================

  * [neat-genreads](#neat-genreads)
  * [Table of Contents](#table-of-contents)
    * [Requirements](#requirements)
    * [Installation] (#installation)
    * [Usage](#usage)
    * [Functionality](#functionality)
    * [Examples](#examples)
      * [Whole genome simulation](#whole-genome-simulation)
      * [Targeted region simulation](#targeted-region-simulation)
      * [Insert specific variants](#insert-specific-variants)
      * [Single end reads](#single-end-reads)
      * [Large single end reads](#large-single-end-reads)
      * [Parallelizing simulation](#parallelizing-simulation)
  * [Utilities](#utilities)
    * [compute_gc.py](#computegcpy)
    * [compute_fraglen.py](#computefraglenpy)
    * [generate_mutation_model.py](#genmutmodelpy)

    * [genSeqErrorModel.py](#genseqerrormodelpy)
    * [plot_mut_model.py](#plotmutmodelpy)
    * [vcf_compare_OLD.py](#vcf_compare_oldpy)
      * [Note on Sensitive Patient Data](#note-on-sensitive-patient-data)


## Requirements

* Python == 3.10.*
* biopython == 1.79
* matplotlib == 3.5.1
* numpy == 1.22.3
* pysam == 0.19.1
* pyyaml == 6.0

## Installation
To install NEAT, you must create a virtual environment using a tool such as conda. Once activated, you can
use the poetry module in build a wheel file, which can then be pip installed. You will need to run these
commands from within the NEAT directory.

```
> conda env create -f environmental.yml -n neat
> conda activate neat
> poetry build
> pip install dist/neat*whl
```

Alternatively, if you wish to work with NEAT in the development environment, you can use poetry install within the
neat repo:
```
> poetry install
```

Test your install by running:
```
> neat --help
```

You should see the neat help message.

## Usage
Here's the simplest invocation of genReads using default parameters. This command produces a single ended fastq file with reads of length 101, ploidy 2, coverage 10X, using the default sequencing substitution, GC% bias, and mutation rate models.

```
neat generate_reads -c neat_config.yaml -o simulated_data
```

The output prefix should not specify a file extension (i.e., .fasta, .fastq, etc.),
as these will be appended by NEAT.

A config file is required. The config is a yaml file specifying the input parameters. The following is a brief
description of the potential inputs in the config file. See NEAT/config_template/template_neat_config.yaml for a
template config file to copy and use for your runs.

reference: full path to a fasta file to generate reads from
read_len: The length of the reads for the fastq (if using). Integer value, default 101.
coverage: desired coverage value. Float or int, default = 10
ploidy: Desired value for ploidy (# of copies of each chromosome). Default is 2
paired_ended: If paired-ended reads are desired, set this to True. Setting this to true requires
    either entering values for fragment_mean and fragment_st_dev or entering the path to a
    valid fragment_model.
fragment_mean: Use with paired-ended reads, set a fragment length mean manually
fragment_st_dev: use with paired-ended reads, set the standard deviation of the fragment length dataset

The following values can be set to true or omitted to use defaults. If True, NEAT will produce the file type.
The default is given:
produce_bam: False
produce_vcf: False
produce_fasta: False
produce_fastq: True

error_model: full path to an error model generated by NEAT. Leave empty to use default model
    (default model based on human, sequenced by Illumina)
mutation_model: full path to a mutation model generated by NEAT. Leave empty to use a default
    model (default model based on human data sequenced by Illumina)
fragment_model: full path to fragment length model generate by NEAT. Leave empty to use default model
    (default model based on human data sequenced by Illumina)
gc_model: Full path to model for correlating GC concentration and coverage, produced by NEAT.
    (default model is based on human data, sequenced by Illumina)


partition_mode: by chromosome ("chrom"), or subdivide the chromosomes ("subdivision").
    Note: this feature is not yet fully implemented
threads: The number of threads for NEAT to use.
    Note: this feature is not yet fully implemented
avg_seq_error: average sequencing error rate for the sequencing machine. Use to increase or
    decrease the rate of errors in the reads. Float betwoon 0 and 0.3. Default is set by the error model.
rescale_qualities: rescale the quality scores to reflect the avg_seq_error rate above. Set True to activate.
include_vcf: full path to list of variants in vcf format to include in the simulation.
target_bed: full path to list of regions in bed format to target. All areas outside these regions will have
    very low coverage.
off_target_scalar: manually set the off-target-scalar when using a target bed. Default is 0.02
    (i.e., off target areas will have only 2% of the average coverage)
discard_offtarget: throws out reads from off-target regions. Regions of overlap may still have reads.
    Set True to activate
discard_bed: full path to a list of regions to discard, in BED format.
mutation_rate: Desired rate of mutation for the dataset. Float between 0 and 0.3
    (default is determined by the mutation model)
mutation_bed: full path to a list of regions with a column describing the mutation rate of that region,
    as a float with values between 0 and 0.3. The mutation rate must be in the third column.
no_coverage_bias: Set to true to produce a dataset free of coverage bias
rng_seed: Manually enter a seed for the random number generator. Used for repeating runs.
min_mutations: Set the minimum number of mutations that NEAT should add, per contig. Default is 1.
fasta_per_ploid: Produce one fasta per ploid. Default behavior is to produce
    a single fasta showing all variants.                                                                                                                                                                        |


## Functionality

![Diagram describing the way that genReads simulates datasets](docs/NEATNEAT.png "Diagram describing the way that genReads simulates datasets")

NEAT produces simulated sequencing datasets. It creates FASTQ files with reads sampled from a provided reference genome, using sequencing error rates and mutation rates learned from real sequencing data. The strength of genReads lies in the ability for the user to customize many sequencing parameters, produce 'golden', true positive datasets, and produce types of data that other simulators cannot (e.g. tumour/normal data).

Features:

- Simulate single-end and paired-end reads 
- Custom read length
- Can introduce random mutations and/or mutations from a VCF file
  - Supported mutation types include SNPs, indels (of any length), inversions, translocations, duplications
  - Can emulate multi-ploid heterozygosity for SNPs and small indels
- Can simulate targeted sequencing via BED input specifying regions to sample from
- Can accurately simulate large, single-end reads with high indel error rates (PacBio-like) given a model
- Specify simple fragment length model with mean and standard deviation or an empirically learned fragment distribution using utilities/computeFraglen.py
- Simulates quality scores using either the default model or empirically learned quality scores using utilities/fastq_to_qscoreModel.py
- Introduces sequencing substitution errors using either the default model or empirically learned from utilities/
- Accounts for GC% coverage bias using model learned from utilities/computeGC.py
- Output a VCF file with the 'golden' set of true positive variants. These can be compared to bioinformatics workflow output (includes coverage and allele balance information)
- Output a BAM file with the 'golden' set of aligned reads. These indicate where each read originated and how it should be aligned with the reference
- Create paired tumour/normal datasets using characteristics learned from real tumour data
- Parallelized. Can run multiple "partial" simulations in parallel and merge results
- Low memory footprint. Constant (proportional to the size of the reference sequence)

## Examples

The following commands are examples for common types of data to be generated. The simulation uses a reference genome in fasta format to generate reads of 126 bases with default 10X coverage. Outputs paired fastq files, a BAM file and a VCF file. The random variants inserted into the sequence will be present in the VCF and all of the reads will show their proper alignment in the BAM. Unless specified, the simulator will also insert some "sequencing error" -- random variants in some reads that represents false positive results from sequencing.

### Whole genome simulation
Simulate whole genome dataset with random variants inserted according to the default model. 

```
[contents of neat_config.yml]
reference: hg19.fa
read_len: 126
produce_bam: True
produce_vcf: True
paired_ended: True
fragment_mean: 300
fragment_st_dev: 30

neat generate_reads                  \
        -c neat_config.yaml          \
        -o /home/me/simulated_reads
```

### Targeted region simulation
Simulate a targeted region of a genome, e.g. exome, with -t.

```
[contents of neat_config.yml]
reference: hg19.fa
read_len: 126
produce_bam: True
produce_vcf: True
paired_ended: True
fragment_mean: 300
fragment_st_dev: 30
targed_bed: hg19_exome.bed

neat generate_reads                 \
        -c neat_config              \
        -o /home/me/simulated_reads
```

### Insert specific variants
Simulate a whole genome dataset with only the variants in the provided VCF file using -v and -M.

```
[contents of neat_config.yml]
reference: hg19.fa
read_len: 126
produce_bam: True
produce_vcf: True
paired_ended: True
fragment_mean: 300
fragment_st_dev: 30
input_variants: NA12878.vcf
mutation_rate: 0

neat generate_reads                 \
        -c neat_config.yml          \
        -o /home/me/simulated_reads
```

### Single end reads
Simulate single end reads by omitting paired ended options.

```
[contents of neat_config.yml]
reference: hg18.fa
read_len: 126
produce_bam: True
produce_vcf: True

neat generate_reads                 \
        -c neat_config.yml          \
        -o /home/me/simulated_reads
```

### Large single end reads
Simulate PacBio-like reads by providing an error model.

```
[contents of neat-config.yml]
reference: hg19.fa
read_len: 5000
error_model: errorModel_pacbio.pickle.gz
avg_seq_error: 0.1

neat generate_reads                 \
        -c neat_config.yml          \
        -o /home/me/simulated_reads
```

# Utilities	
Several scripts are distributed with gen_reads that are used to generate the models used for simulation.

## neat compute_gc_bias

Computes GC% coverage bias distribution from sample (bedrolls genomecov) data.
Takes .genomecov files produced by BEDtools genomeCov (with -d option).

```
bedtools genomecov
        -d                          \
        -ibam normal.bam            \
        -g reference.fa
```

```
neat compute_gc_bias                \
        -r reference.fa             \
        -i genomecovfile            \
        -w [sliding window length]  \
        -o /path/to/prefix
```

## neat create_fraglen_model

Computes empirical fragment length distribution from sample data.
Takes SAM/BAM file via stdin:

    neat create_fraglen_model   \
        -i input.bam            \
        -o /prefix/for/output

and creates fraglen.pickle.gz model in working directory.

## neat create_mutation_model

Takes references genome and VCF file to generate mutation models:

```
neat creaet_mutation_model          \
        -r hg19.fa                  \
        -m inputVariants.vcf        \
        -o /home/me/models
```

Trinucleotides are identified in the reference genome and the variant file. Frequencies of each trinucleotide transition are calculated and output as a pickle (.p) file.

| Option          | Description                                                                  |
|-----------------|------------------------------------------------------------------------------|
| -r <str>        | Reference file for organism in FASTA format. Required                        |
| -m <str>        | Mutation file for organism in VCF format. Required                           |
| -o <str>        | Path to output file and prefix. Required.                                    |
| --bed           | Flag that indicates you are using a bed-restricted vcf and fasta (see below) |
| --save-trinuc   | Save trinucleotide counts for reference                                      |
| --human-sample  | Use to skip unnumbered scaffolds in human references                         |
| --skip-common   | Do not save common snps or high mutation areas                               |


## neat generate_error_model

Generates sequencing error model for neat.
This script needs revision, to improve the quality-score model eventually, and to include code to learn sequencing errors from pileup data.

```
neat generate_error_model                             \
        -i input_read1.fq (.gz) / input_read1.sam     \
        -o /output/prefix                             \
        -i2 input_read2.fq (.gz) / input_read2.sam    \
        -p input_alignment.pileup                     \
        -q quality score offset [33]                  \
        -Q maximum quality score [41]                 \
        -n maximum number of reads to process [all]   \
        -s number of simulation iterations [1000000]  \
        --plot perform some optional plotting
```

## neat plot_mutation_model

Performs plotting and comparison of mutation models generated from genMutModel.py.

```
neat plot_mutation_model                                                \
        -i model1.pickle.gz [model2.pickle.gz] [model3.pickle.gz]...    \
        -l legend_label1 [legend_label2] [legend_label3]...             \
        -o path/to/pdf_plot_prefix
```

## neat vcf_compare

Tool for comparing VCF files.

```
neat vcf_compare
        -r <ref.fa>        * Reference Fasta                           \
        -g <golden.vcf>    * Golden VCF                                \
        -w <workflow.vcf>  * Workflow VCF                              \
        -o <prefix>        * Output Prefix                             \
        -m <track.bed>     Mappability Track                           \
        -M <int>           Maptrack Min Len                            \
        -t <regions.bed>   Targetted Regions                           \
        -T <int>           Min Region Len                              \
        -c <int>           Coverage Filter Threshold [15]              \
        -a <float>         Allele Freq Filter Threshold [0.3]          \
        --vcf-out          Output Match/FN/FP variants [False]         \
        --no-plot          No plotting [False]                         \
        --incl-homs        Include homozygous ref calls [False]        \
        --incl-fail        Include calls that failed filters [False]   \
        --fast             No equivalent variant detection [False]
```
Mappability track examples: https://github.com/zstephens/neat-repeat/tree/master/example_mappabilityTracks

### Note on Sensitive Patient Data
ICGC's "Access Controlled Data" documention can be found at http://docs.icgc.org/access-controlled-data. To have access to controlled germline data, a DACO must be
submitted. Open tier data can be obtained without a DACO, but germline alleles that do not match the reference genome are masked and replaced with the reference
allele. Controlled data includes unmasked germline alleles.



