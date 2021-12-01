'''
Written by Chiann-Ling Cindy Yeh, updated 12/1/2021
Disclaimer: I have not actually tested this script since my construct is a little more unique and requires a different set up. 
This script translates variant sequences to the amino acid sequence and outputs two barcode maps: barcode-translated variant map and barcode-mutations map.

Arguments:
1. barcode variant map, output from PacRAT
2. wild-type variant fasta file
3. name of output file with barcode + translated sequences
4. name of output file with barcode + mutations only
'''

# this script gets mutations of ste5 and ste7 in the subassembly file (subassembly with both doped variants. also generates a translated map

from Bio import SeqIO
from Bio.Seq import Seq
import sys

infile = open(sys.argv[1],"r") # barcode variant map, output from PacRAT
ref = open(sys.argv[2],"r") # wild-type variant fasta file
outfile1 = open(sys.argv[3],"w+") # output file with barcode + translated sequences
outfile2 = open(sys.argv[4],"w+") # output file with barcode + mutations only

ref_seq = SeqIO.parse(ref,"fasta")
ref_seq = ref_seq[0].seq
ref_seq_aa = ref_seq.translate()
ref_seq_aa = str(ref_seq_aa)
ref_seq = str(ref_seq)

var_nt_bc_dict = {}
var_aa_bc_dict = {}

for line in infile:
	line1 = line.strip().split()
	bc = line1[0]
	var = Seq(line1[1])
	var_aa = str(var.translate())
	var = str(var)
	outfile1.write(bc + "\t" + var_aa + "\n")
	
	var_nt_bc_dict[bc] = []
	for i in range(len(var)):
		if ref_seq[i] != var[i]:
			var_nt_bc_dict[bc].append(ref_seq[i] + str(i+1) + var[i])
	if len(var_nt_bc_dict[bc]) == 0:
		var_nt_bc_dict[bc].append("WT")
	var_aa_bc_dict[bc] = []
	for i in range(len(ref_seq_aa)):
		if ref_seq_aa[i] != var_aa[i]:
			var_aa_bc_dict[bc].append(ref_seq_aa[i] + str(i+1) + var_aa[i])
	if len(var_aa_bc_dict[bc]) >= 7:
		var_aa_bc_dict[bc] = ["FS"] # FS = frameshift
	if len(var_aa_bc_dict[bc]) == 0:
		if "WT" in var_nt_bc_dict[bc]:
			var_aa_bc_dict[bc].append("WT")
		else:
			var_aa_bc_dict[bc].append("SYN") # synonymous
	
	var_aa_joined = ",".join(var_aa_bc_dict[bc])
	outfile2.write(bc + "\t" + var_aa_joined + "\n")
		
