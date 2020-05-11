#!/usr/bin/env python3

import gzip
import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
import gzip
import sys

def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

def cal_kd(seq):
    kd=0
    for nt in seq:
        if nt==	"I"	:	kd+=4.5
        elif nt ==	"V"	:	kd+=4.2
        elif nt ==	"L"	:	kd+=3.8
        elif nt ==	"F"	:	kd+=2.8
        elif nt ==	"C"	:	kd+=2.5
        elif nt ==	"M"	:	kd+=1.9
        elif nt ==	"A"	:	kd+=1.8
        elif nt ==	"G"	:	kd+=-0.4
        elif nt ==	"T"	:	kd+=-0.7
        elif nt ==	"S"	:	kd+=-0.8
        elif nt ==	"W"	:	kd+=-0.9
        elif nt ==	"Y"	:	kd+=-1.3
        elif nt ==	"P"	:	kd+=-1.6
        elif nt ==	"H"	:	kd+=-3.2
        elif nt ==	"E"	:	kd+=-3.5
        elif nt ==	"Q"	:	kd+=-3.5
        elif nt ==	"D"	:	kd+=-3.5
        elif nt ==	"N"	:	kd+=-3.5
        elif nt ==	"K"	:	kd+=-3.9
        elif nt ==	"R"	:	kd+=-4.5
    return kd/len(seq)

def hydro_tf(seq,nmer,mean_kd):
    for i in range(0,len(seq)-nmer+1,1):
        seq_mers = seq[i:i+nmer]
        kd = cal_kd(seq_mers)
        if kd > mean_kd:
            return True
    return False


filename = sys.argv[1]
for name, seq in read_fasta(filename):
    if hydro_tf(seq[0:30],8,2.5) and hydro_tf(seq[30:len(seq)],11,2) is True:
        print(name)

"""
python3 transmembrane.py proteins.fasta.gz
18w
Dtg
Krn
Lac
Mcr
PRY
Pxt
Pzl
QC
Ror
S1P
S2P
Spt
apn
bai
bdl
bou
bug
cue
drd
ft
grk
knk
ksh
m
nac
ort
rk
smo
thw
tsg
waw
zye
"""
