# barseq
Analyzing barseq data retrieved from Illumina sequencing

Your read primers should be adjacent to where your barcode is so that the first base pairs are the barcodes for your constructs. 

**Demultiplex samples based on Illumina indices.**

The extension for this will be `fastq.gz`. For the Dunham lab, if you need help demultiplexing, Noah knows how to do this. For others, you can refer to the [demultiplexing documentation here](https://support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/bcl2fastq/bcl2fastq_letterbooklet_15038058brpmi.pdf) or search for the software `bcl2fastq`.

**Merging fastq files**

If you have paired-end reads, you will need to merge your Read1 and Read2 fastq files. Once you have your samples, unzip your folders. You can do this by running `gunzip my_reads_file.fastq.gz` and replacing "my_reads_file" with your own file name. Next, run the `merge_reads/pair_reads.sh` script. Make sure this is running in the same folder as the `merge_reads/trim_reads.py` script. The `pair_reads.sh` script takes four arguments: 1) R1 fastq file path and name, 2) R2 fastq file path and name, 3) barcode length, and 4) sample name. *Note: This will only work if your R1 and R2 primers are absolutely adjacent to your barcode. Please refer to the [PEAR documentation](https://cme.h-its.org/exelixis/web/software/pear/doc.html) if you have different levels of overlap.*

If you have single-end reads, you can just run the `trim_reads.py` script with your fastq file. First argument is your file name, second argument is barcode length.

**Making a data frame for a collector's curve**

If you want to know if you've gotten sufficient coverage for your sequencing run, you can create a collector's curve. Use the script `misc_scripts/collector_curve.py`.

**Count unique barcodes, compare to barcode-variant map**

Use the script `misc_scripts/count_unique_bcs.py`. Be sure to edit script if you want to run this without a barcode-variant map (see script for details).

**Collapse barcode counts by variant**

Use the script `variant_coverage/collapse_bcs.py` to determine how much coverage you have per variant. See script for details on input/output files.

**Translate sequences and get mutations**

Use the script `misc_scripts/get_mutations.py`. See script header for details on input/output files.

**Generating new index barcodes (or barcodes in general) while avoiding overlap with existing indices in Dunham lab**

Use script `generate_new_index/make_index.py`. See script header for details. An existing .txt file contains barcodes (last updated 3/8/22 from custom_indices file in Dunham Shared Drive); please update it if more barcodes have been added since. Scripts `editdist.py` contains the function for calculating edit ditance, no need to install additional packages.
