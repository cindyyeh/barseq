#!/bin/bash
#$ -S /bin/bash
#$ -l mfree=12G -l h_rt=48:0:0
#$ -cwd
#$ -N merge_reads

: "
Using PEAR to merge overlapping Fastq files from barcode sequencing.
Written by Chiann-Ling Cindy Yeh, updated 11/22/2021
This script trims and merges paired-end reads and works with GS grid CentOS7, but can be modified for any server submission system
Make sure trim_reads.py is in the same working directory
***** Your output files will end with '_merged.assembled.fastq'
"

module load pear/0.9.11 # update or change this to work with your cluster server. 

# cd /net/dunham/vol2/Cindy/SUL1_alleleLibraryCompetition/results/19-08-13_barseq_60_62 # CHANGE

: "
Specify the file names/barcode size/sample name while running the script. This is what you would run on UNIX:
qsub pair_reads.sh my_R1_file.fastq my_R2_file.fastq 12 my_sample
"
FREAD=$1 # unzipped file for Read 1
RREAD=$2 # unzipped file for Read 2
BCSIZE=$3 # barcode size, e.g., 12
SAMPLENAME=$4 # what you want the base name of your files to be

: "
If you don't want to specify the files each time, you can replace the variables ($1, $2, $3, $4) below with your file names/barcode sample/sample name like so:
FREAD=my_R1_file.fastq # unzipped file for Read 1
RREAD=my_R2_file.fastq # unzipped file for Read 2
BCSIZE=12 # barcode size, e.g., 12
SAMPLENAME=my_sample # what you want the base name of your files to be
"

python trim_reads.py ${FREAD} ${BCSIZE}
python trim_reads.py ${RREAD} ${BCSIZE} #output is ${RREAD}_trimmed.fastq 

# FREAD2=$(echo ${FREAD} | cut -f 1 -d '.')
# RREAD2=$(echo ${RREAD} | cut -f 1 -d '.')
# these retrieve the basename of your fastq files
FREAD2=$(basename -- "$FREAD")
FREAD2="${FREAD2%.*}"
RREAD2=$(basename -- "$RREAD")
RREAD2="${RREAD2%.*}"
# echo $FREAD2
# echo $RREAD2

pear -v ${BCSIZE} -n ${BCSIZE} -m ${BCSIZE} -f ${FREAD2}_trimmed.fastq -r ${RREAD2}_trimmed.fastq -o ${SAMPLENAME}_merged

# This section can be commented out if you want to keep the intermediate files. I usually don't.
rm ${SAMPLENAME}_merged.discarded.fastq
rm ${SAMPLENAME}_merged.unassembled.forward.fastq
rm ${SAMPLENAME}_merged.unassembled.reverse.fastq
rm *_trimmed.fastq

