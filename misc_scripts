"""
Written by Clara J. Amorosi, updated 11/22/2021 by Chiann-Ling Cindy Yeh
This script generates a file that can be used to plot a collector curve, where the x axis is the first column and the y axis is the second column.

This script has the following arguments:
	sys.argv[1] = list of barcodes (one per line) or a trimmed fastq file. must be unzipped
	sys.argv[2] = specify output file name
	sys.argv[3] = specify fastq or txt
"""

import sys
import numpy as np
from numpy import *

barcodes = open(sys.argv[1], 'r') # fastq file trimmed to only barcodes
outfile = open(sys.argv[2], 'w')
filetype = sys.argv[3]

outdata=[]
bardict={}

count = 0

if sys.argv[3] == "fastq":
	while True:
		line = barcodes.readline()
		bc = barcodes.readline().strip()
		line = barcodes.readline()
		line = barcodes.readline()
		if line == "":
			break
		if bc in bardict:
			outdata += [count]
		else:
			bardict[bc] = 1
			count += 1
			outdata += [count]
else:
	for line in barcodes:
		currBC = line.strip().split()
		currBC = currBC[0]
		if currBC in bardict:
			outdata += [count]
		else:
			bardict[currBC] = 1
			count += 1
			outdata += [count]

barcodes.close()

for i in range(len(outdata)):
    outfile.write(str(i)+"\t"+str(outdata[i])+"\n")

outfile.close()
