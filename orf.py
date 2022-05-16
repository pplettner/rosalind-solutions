#!/usr/local/bin/python3

import argparse
from utils import read_fasta, rna_to_prot

def dna_to_rna(string):
    trans_table = str.maketrans('T','U')
    rna_string = string.upper().translate(trans_table)
    return rna_string

def orf(seq):
    start = 0
    protein_seqs = set()

    while (location := seq.find('AUG', start)) != -1:
        start = location + 3
        protein_seq = rna_to_prot(seq[location:])
        protein_seqs.add(protein_seq)

    return protein_seqs

def reverse_complement(string):
    trans_table = str.maketrans('ACGT','TGCA')
    revc = string.upper()[::-1].translate(trans_table)
    return revc


parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

(name, seq) = next(read_fasta(args.dataset))

rna_seq = dna_to_rna(seq)
revc_rna_seq = dna_to_rna(reverse_complement(seq))

candidates = set()

for s in (rna_seq, revc_rna_seq):
    candidates.update(orf(s))

print ('\n'.join(candidates))