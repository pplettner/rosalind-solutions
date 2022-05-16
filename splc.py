#!/usr/local/bin/python3

import argparse
from utils import read_fasta, rna_to_prot
    
def dna_to_rna(string):
    trans_table = str.maketrans('T','U')
    rna_string = string.upper().translate(trans_table)
    return rna_string

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

fa_iter = read_fasta(args.dataset)

(name, seq) = next(fa_iter)

for (name, intron) in fa_iter:
    seq = seq.replace(intron, '')

rna_seq = dna_to_rna(seq)
protein_seq = rna_to_prot(rna_seq)

print (protein_seq)