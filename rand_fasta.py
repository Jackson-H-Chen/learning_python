#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line:
#	python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>


"""
python3 rand_fasta.py 3 10 20 0.1 0.2 0.3 0.4
>seq-0
TCGTTTTGATTACGG
>seq-1
CGGCTGTTCCGTAATGC
>seq-2
TTTCGTGTACTTTCTAGTGA
"""
count = int(sys.argv[1])
pct_a = float(sys.argv[4])
pct_t = float(sys.argv [7])
pct_c = float(sys.argv [5])
pct_g = float(sys.argv [6])
min_seq_len = int(sys.argv [2])
max_seq_len = int(sys.argv [3])

#assert variable
assert float(1) == float(pct_t+pct_a+pct_c+pct_g)
assert (min_seq_len > 0) is True
assert (min_seq_len < max_seq_len) is True

#define random sequence function
def ran_seq(pct_a,pct_t,pct_g,pct_c,min_seq_len,max_seq_len):
    dna_seq = []
    dna_seq_len = random.randint(min_seq_len,max_seq_len)
    for i in range(dna_seq_len):
        j = random.random()
        if j >= pct_t + pct_g + pct_c : dna_seq.append('A')
        elif j >= pct_t + pct_g : dna_seq.append('C')
        elif j >= pct_t : dna_seq.append('G')
        else: dna_seq.append('T')
    return ''.join(dna_seq)

#Output
for k in range(count):
    dna = ran_seq(pct_a,pct_t,pct_g,pct_c,min_seq_len,max_seq_len)
    print(f'{">seq-"}{k}')
    print(f'{dna}')
