#!/usr/bin/env python



#NAME: percent_nucleotide.py


#This Python program calculates the perecentage composition of each nucleotide in a user-specified nucleic acid sequence



#This is a new .py file that I created in my remote Github Collaboration_Percent_Nucleotide branch that I will pull from my local repository to collaborate and edit a script that 
#will calculate % nucleotide in a user-entered sequence. This is done to avoid  cloning repositories



import sys, re
from argparse import ArgumentParser

#Creating parser to parse command-line argument
parser = ArgumentParser(description='Calculate the percentage of each nucleotide in a user-entered nucleic acid sequence')

#Parsing arguments
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")

#If command-line arguments length is 1, print help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

#Convert sequence to upper-case
args.seq = args.seq.upper()

#Checking for valid nucleic acid sequence containing A,G,C,T, or U
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and re.search('U', args.seq):
        print('Your sequence contains both U and T and is therefore hybrid RNA/DNA')
    elif re.search('U', args.seq):
        print('Your sequence is RNA')
    elif re.search('T', args.seq):
        print('Your sequence is DNA')
    #Checking if sequence contains A,C,G but no T or U:
    else:
        print ('Your sequence contains A,C,or G, but it does not contain T or U. Therefore, it can be either DNA or RNA')
    # Calculating the percentage of each nucelotide
    #Calculating sequence length and initialization:
    sequence_length = len(args.seq)
    nucleotide_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'U': 0}

    # For loop iteration and incrementing:
    for nucleotide in args.seq:
        nucleotide_count[nucleotide] += 1

    # Calculation and output:
    print("Percentage of each nucleotide:")
    for nucleotide, count in nucleotide_count.items():
        percentage = (count / sequence_length) * (100)
        print(f"{nucleotide}: {percentage:.2f}%")
else:
    print('Your sequence is not a valid nucleic acid sequence')


