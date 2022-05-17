#!/usr/local/bin/python3

import argparse
from utils import dna_to_rna,read_fasta,rna_to_prot

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

fa_iter = read_fasta(args.dataset)

(_, seq) = next(fa_iter)

for (_, intron) in fa_iter:
    seq = seq.replace(intron, '')

rna_seq = dna_to_rna(seq)
protein_seq = rna_to_prot(rna_seq)

print (protein_seq)