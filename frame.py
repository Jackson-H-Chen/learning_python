#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'
position = 0
frame = -1
#single loop
print ("position", "frame", "letter")
for position in range (0, len(dna), 3) :
    frame += 1
    position += 1
    Letter = dna[position-1:position]
    print (position-1, frame, Letter)
    frame += 1
    position += 1
    Letter = dna[position-1:position]
    print (position-1, frame, Letter)
    frame += 1
    position += 1
    Letter = dna[position-1:position]
    print (position-1, frame, Letter)
    frame -= 3
#nested loop
dna = 'ATGGCCTTT'
position = 0
frame = 0, 1, 2
print ("position", "frame", "letter")
for position in range (0, len(dna), 3) :
    for frame in range (0, 3, 1) :
        position += 1
        Letter = dna[position-1:position]
        print (position-1, frame, Letter)
"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
