#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it
# We will have a variable number of bins (can be months or days)
# And some number of trials for the simulation
# And some number of people whose have random birthdays
# Use assert() to check parameters
# On the command line:
#	python3 birthday.py <bins> <trials> <people>


"""
python3 birthday.py 365 1000 23
0.520
"""
import sys
import random

days = int(sys.argv[1])
trials = int(sys.argv[2])
people = int(sys.argv[3])
hits = 0
for i in range(trials):
    pool = []
    for j in range(days):
        pool.append(0)
    for k in range(people):
        pool[random.randint(0,days-1)] +=1
    for count in pool:
        if count >= 2:
            hits += 1
            break
print(f'{hits/trials}')
