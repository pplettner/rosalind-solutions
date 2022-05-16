#!/usr/local/bin/python3

import argparse
from collections import defaultdict
from utils import PROTEIN_OF_CODON

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()


num_codons = defaultdict(int)

for codon,protein in PROTEIN_OF_CODON.items():
    num_codons[protein] += 1

protein_seq = args.dataset.read().strip()

num_combos = 1

for protein in protein_seq:
    num_combos *= num_codons[protein]
    num_combos %= 1000000

num_combos *= num_codons['Stop']
print (num_combos % 1000000)