'''
Written by Chiann-Ling Cindy Yeh, updated 11/30/2021
This script groups barcodes by variants and counts how many reads are associated with each variant; works with maps where a barcode is being mapped to more than one gene (e.g., Ste5 and Ste7 on the same amplicon with the barcode)
First argument: path to tab-delimited barcode-variant map (first column barcode, other columns contain variant info. doesn't necessarily have to be a sequence (can be unique identifier). aka output from PacRAT https://github.com/dunhamlab/PacRAT )
Second argument: path to tab-delimited barcode-counts file (first column barcode, sequence column counts, aka the output of misc_scripts/count_unique_bcs.py)
Third argument: name of output file

Output file: 
column 1: variant
column 2: number of barcodes matched to this variant from pacbio
column 3: number of barcodes matched to this variant from pacbio that are also found in barseq counts
column 4: number of read counts for this variant over all barcodes
'''


import sys

var_map_infile = open(sys.argv[1],"r") # this input is the link to the tab-delimited barcode-variant map
var_bc_dict = {}
for line in var_map_infile:
	line = line.strip().split()
	if len(line) > 2: # if barcode represents more than one variant
		bc = line[0]
		var = ";".join(line[1:])
	else:
		bc = line[0]
		var = line[1]
	if var not in var_bc_dict:
		var_bc_dict[var] = [bc]
	else:
		var_bc_dict[var].append(bc)
var_map_infile.close()
print(len(var_bc_dict))


bc_count_file = open(sys.argv[2],"r")
bc_count_dict = {}
for line in bc_count_file:
	line = line.strip().split()
	bc_count_dict[line[0]] = int(line[1])
bc_count_file.close()

print(len(bc_count_dict))

outfile = open(sys.argv[3],"w+") 
var_counts_dict = {}
for key in var_bc_dict:
	counts = 0
	num_bcs = 0
	num_bcs_counted = 0
	for bc in var_bc_dict[key]:
		num_bcs += 1
		if bc in bc_count_dict:
			counts += bc_count_dict[bc]
			num_bcs_counted += 1
	var_counts_dict[key] = counts
	outfile.write(key + "\t" + str(num_bcs) + "\t"+ str(num_bcs_counted) + "\t" + str(counts) + "\n")

	



