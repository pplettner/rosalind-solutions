#!/usr/local/bin/python3

import argparse
from utils import dna_to_rna,read_fasta,reverse_complement,rna_to_prot

def orf(seq):
    start = 0
    protein_seqs = set()

    while (location := seq.find('AUG', start)) != -1:
        start = location + 3
        protein_seq = rna_to_prot(seq[location:])
        protein_seqs.add(protein_seq)

    return protein_seqs

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