"""
This script counts number of unique barcodes for a trimmed/pear-ed fastq file
Written by Chiann-Ling Cindy Yeh, updated 11/22/2021

This script takes four arguments:
1. path to trimmed fastq file
2. name that you want output file to be. lists barcode in first column and number of occurences of that barcode in second column. 
3. path to barcode-variant map. if this is unavailable, comment out line 16 and lines 47-56
4. what you want the count filter to be (e.g., if you want to ignore barcodes that only appear once, your filter will be 2)
"""

import sys

infile = open(sys.argv[1],"r") # trimmed fastq file
outfile = open(sys.argv[2],"w+") # outfile that lists barcode in first column and number of occurences of that barcode in second column
infile2 = open(sys.argv[3],"r") # path to barcode-variant map
count_filter = sys.argv[4] # 
bcs = {}

while True:
	infile.readline()
	bc = infile.readline().strip()
	#print(seq)
	if bc == "":
		break
	if bc not in bcs:
		bcs[bc] = 1
	else:
		bcs[bc] += 1
	infile.readline()
	infile.readline()

unique_barseq_bcs = bcs.keys()
print("unique barcodes (no filter): " + str(len(unique_barseq_bcs)))

count_unique_filtered = 0
for key in bcs:
	if bcs[key] >= int(count_filter):
		count_unique_filtered += 1
		outfile.write(key + "\t" + str(bcs[key]) + "\n")
print("unique barcodes (filter threshold " + count_filter + "): " + str(count_unique_filtered))


# compare this list to pacbio data
#infile2 = open("../ste5_ste7_np3_subassembly.txt","r")

unique_pacbio_bcs = []
for line in infile2:
	line = line.strip().split()
	bc = line[0]
	unique_pacbio_bcs.append(bc)
	
unique_pacbio_bcs = list(set(unique_pacbio_bcs))

common = len(list(set(unique_barseq_bcs).intersection(unique_pacbio_bcs)))
print("num barcodes found in pacbio subassembly: " + str(common))
