#!/usr/bin/env python

#SHE-BANG!

#NAME: seqClass.py

#NUCLEIC ACID CLASSIFICATION 
#THIS PYTHON SCRIPT DETERMINES IF A USER-SPECIFIED LETTER SEQUENCE IS DNA, RNA, OR NEITHER NUCLEIC ACID
#(USE -s COMMAND-LINE SEQUENCE ARGUMENT AT PROGRAM EXECUTION).THIS PYTHON SCRIPT ALSO DETERMINES IF  
#ANOTHER USER-ENTERED LETTER SEQUENCE IS A MOTIF LOCATED IN AFOREMENTIONED "LARGER" SEQUENCE 
#(USE -m MOTIF COMMAND-LINE ARGUMENT AT PROGRAM EXECUTION).THIS PYTHON SCRIPT WAS EDITED VIA VI EDITOR 
#IN A LOCAL FIX BRANCH AND SUBSEQUENTLY LINEAR-FORWARD MERGED WITH MASTER BRANCH AND PUSHED TO THIS REMOTE GITHUB REPOSITORY


import sys, re
from argparse import ArgumentParser

# Parser to parse command-line arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA or something else')

# Adding command-line arguments for sequences
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input Sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Input Motif")

#Print help and exit if user provides no arguments:
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

#Parsing command-line arguments
args = parser.parse_args()


args.seq = args.seq.upper()                 # Note we added this line previously to convert any lower-case characters of user-input sequence to uppercase 

#Checking if sequence is valid sequence containing nucleotides A,C,G,T, or U
if re.search('^[ACGTU]+$', args.seq):
    #Checking if sequence contains both T and U
    if re.search('T', args.seq) and re.search('U', args.seq):
        print ('Your sequence contains both T and U. This is either a result of data-entry error, mutation, incomplete reverse transcription, incomplete transcription, or alien hybrid nucleic acid')
    elif re.search('U', args.seq):
        print ('Your sequence is RNA')
    elif re.search('T', args.seq):
        print ('Your sequence is DNA')
    #Checking if sequence contains A,C,G but no T or U:
    else:
        print ('Your sequence contains A,C,or G, but it does not contain T or U. Therefore, it can be either DNA or RNA')
    #Checking invalid non-nucleic acid sequence:
else:
    print ('The sequence is neither DNA nor RNA')

#The following statement was added per Task 17 to state that the following code alerts if a motif is found or not
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    #CHECKING TO ENSURE LENGTH OF MOTIF IS SMALLER THAN LENGTH OF SEQUENCE
    if len(args.motif)>len(args.seq):
        print(f'Motif is longer than sequence. Please re-enter and re-execute')
        parser.print_help()
        sys.exit(1)
    if re.search(args.motif, args.seq):

        print("MOTIF FOUND IN SEQUENCE")

    else:
        print("MOTIF NOT FOUND IN SEQUENCE")
