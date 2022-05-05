#!/usr/local/bin/python3

import argparse
import json
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('-c','--codon', help='Codon mapping json', type=argparse.FileType('r'), required=True)
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()


protein_of_codon = json.load(args.codon)
num_codons = defaultdict(int)

for codon,protein in protein_of_codon.items():
    num_codons[protein] += 1

protein_seq = args.dataset.read().strip()

num_combos = 1

for protein in protein_seq:
    num_combos *= num_codons[protein]
    num_combos %= 1000000

num_combos *= num_codons['Stop']
print (num_combos % 1000000)