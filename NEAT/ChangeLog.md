# NEAT has a new home
NEAT is now a part of the NCSA github and active development will continue here. Please direct issues, comments, and requests to the NCSA issue tracker. Submit pull requests here insead of the old repo.

# NEAT v3.1

Bug Fixes:
- Fixed an issue where NEAT could not read in gzipped vcf files
- Fixed a bug where NEAT was assuming a ploidy of 2
- Fixed a bug that was causing NEAT to produce exactly the same reverse strands as forward strands in paired ended mode
- Fixed a bug when reading in some mutation models.
- Added gzipping to all mutation models to maximize their compression
- Fixed some issues with vcf_compare

# NEAT v3.0
- NEAT gen_reads now runs in Python 3 exclusively. The previous, Python 2 version is stored in the repo as v2.0, but will not be undergoing active development.
- Converted sequence objects to Biopython Sequence objects to take advantage of the Biopython library
- Converted cigar strings to lists. Now there are simply a functions that convert a generic cigar string to a list and vice versa.
- Tried to take better advantage of some Biopython libraries, such as for parsing fastas.
- For now, we've eliminated the "Jobs" option and the merge jobs function. We plan to implement multi-threading instead as a way to speed up NEAT's simulation process.
- Added a basic bacterial wrapper that will simulate multiple generations of bacteria based on an input fasta, mutate them and then produce the fastqs, bams, and vcfs for the resultant bacterial population.

For improvements, we have a lot of great ideas for general improvements aimed at better simulating bacteria, but we believe this same improvements will have applications in other species as well. 
- Multiploidy - all right this has nothing to do with bacteria specifically, but it is a feature we would like to implement into gen_reads.
- Structural Variants - model large scale structural variants with an eye toward intergenic SVs.
- Transposable Elements - model transposons within the sequence
- Repeat regions - will bring a variety of interesting applications