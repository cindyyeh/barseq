# this script shortens fastq files while retaining quality scores/read identifiers
# Written by Chiann-Ling Cindy Yeh, updated 11/22/2021

import sys
import re
import random

fastq_file = open(sys.argv[1],"r")
read_length = int(sys.argv[2])

basename = re.split("/",sys.argv[1])
basename = basename[-1]
basename = re.split("\.",basename)
basename = basename[0]
print(basename)
fastq_trimmed_name = basename+"_trimmed.fastq"
fastq_trimmed = open(fastq_trimmed_name,"w+")

iter = 0
bases = ["A","C","G","T"]

while True:		
	readname = fastq_file.readline()
	sequence = fastq_file.readline()
	fastq_file.readline()
	quality = fastq_file.readline()
	
	#preseq = random.choice(bases)+random.choice(bases)+random.choice(bases)+random.choice(bases)+random.choice(bases)
	if not sequence:
		break
# 	if readname[0] != "@" or not readname: #break if end of line
# 		break
	sequence = sequence[0:read_length]
	quality = quality[0:read_length]
	
	fastq_trimmed.write(readname+sequence+"\n+\n"+quality+"\n")
	
	if iter % 100000 == 0:
		print(iter)
	iter += 1
	
fastq_file.close()
fastq_trimmed.close()

