#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# Use fileinput to get the data from nucleotides.txt
# Make sure that the values are probabilities
# Make sure that the distribution sums to 1
# Report with 3 decimal figures


"""
python3 entropy.py nucleotides.txt
1.846
"""
import sys
import math
import fileinput
file = sys.argv[1]
data = []
sum = 0
for line in fileinput.input(file):
    if line.startswith('#'): continue
    col = line.split()
    pct = float(col[1])
    assert (pct >= 0 and pct <= 1) is True
    sum += pct
    data.append(pct)
assert(math.isclose(sum,1))
entropy = 0
for i in range(len(data)):
    entropy += data[i]*math.log2(data[i])
print(f'{-entropy:.3f}')
