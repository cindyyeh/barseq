"""
This program generates strings that are N mutations away from each other
for making unique index strings

Written by Anna Sunshine
Edited by Cindy Yeh

First input: text file with one column that has all listed barcodes to avoid overlap
Second: name of output file
***** EDIT: Please change the second value in line 23 (line_string) if barcode is of a different length *****
"""

import sys
import editdist
import random

input_strings_file = open(sys.argv[1], "r") #file with any pre-existing strings
output_file = open(sys.argv[2], "w")

#create list of existing strings
string_list = []
for line in input_strings_file:
        line_string = line[0:8] #HOW LONG IS THE BARCODE?
        string_list.append(line_string)

nuc_list = ["A","C","G","T"]

output_counter = 0
while output_counter < 2: # HOW MANY BARCODES ARE NEEDED ?
        bp_counter = 0
        index_list = []
        while bp_counter < 8: # HOW LONG IS THE BARCODE?
                number = random.randint(0,3)
                nuc = nuc_list[number]
                index_list.append(nuc)
                bp_counter = bp_counter+1
        
        query_string = ''.join(index_list)
        
        mut_counter = 0
        for element in string_list:
                distance = editdist.LD(query_string, element)
                if distance < 3:
                        mut_counter = mut_counter + 1
        
        if mut_counter < 1:
                newline = query_string + "\n"
                output_file.write(newline)
                string_list.append(query_string)
                output_counter = output_counter +1
                
input_strings_file.close()
output_file.close()
