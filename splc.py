#!/usr/local/bin/python3

import argparse
import json
from itertools import zip_longest
from utils import read_fasta

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)
    
def dna_to_rna(string):
    trans_table = str.maketrans('T','U')
    rna_string = string.upper().translate(trans_table)
    return rna_string

def rna_to_prot(seq, protein_of_codon):
    protein_seq = ''
    for triple in grouper(seq, 3):
        codon = ''.join(triple)
        protein = protein_of_codon[codon]

        if protein == 'Stop':
            break
        else:
            protein_seq += protein
    return protein_seq

parser = argparse.ArgumentParser()
parser.add_argument('-c','--codon', help='Codon mapping json', type=argparse.FileType('r'), required=True)
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

fa_iter = read_fasta(args.dataset)
protein_of_codon = json.load(args.codon)

(name, seq) = next(fa_iter)

for (name, intron) in fa_iter:
    seq = seq.replace(intron, '')

rna_seq = dna_to_rna(seq)
protein_seq = rna_to_prot(rna_seq, protein_of_codon)

print (protein_seq)