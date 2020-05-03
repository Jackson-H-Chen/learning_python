#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!
datainput = []
count = 0
for line in fileinput.input():
    if line.startswith('#'): continue
    line = line.rstrip()
    datainput.append(float(line))
    count += 1
datainput.sort()
max = datainput[-1]
min = datainput [0]
sum = sum(datainput)
mean = sum/count
tsqrdistance = 0
for numbers in datainput:
    sqrdiastance = (numbers-mean)**2
    tsqrdistance += sqrdiastance
std = sqrt(tsqrdistance/count)
center = (count+1) / 2
if center.is_integer() is True:
    center = count // 2
    median = datainput [center]
else:
    gcenter = int(round(center))
    lcenter = int(gcenter - 1)
    median = (datainput[gcenter-1] + datainput[lcenter-1])/2
print(f'count:  {count}')
print(f'Minimum:    {min}')
print(f'Maximum:    {max}')
print(f'Mean:   {mean}')
print(f'Std. dev:   {std:.3f}')
print(f'Median:  {median}')

#OSFrog

"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
