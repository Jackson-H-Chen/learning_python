#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence
seq=[]
at_count = 0
for i in range(0,30):
    r = random.randint(0,100)
    if r <= 60 and r >= 30:
        seq.append ('A')
        at_count += 1
    elif r < 30:
        seq.append ('T')
        at_count += 1
    elif r >= 80:
        seq.append ('G')
    else:
        seq.append ('C')
seq=''.join(seq)
print(f'{"30"} {at_count/30} {seq}')

"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
