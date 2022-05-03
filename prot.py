#!/usr/local/bin/python3

import argparse
import json
from itertools import takewhile, zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

parser = argparse.ArgumentParser()
parser.add_argument('-c','--codon', help='Codon mapping json', type=argparse.FileType('r'), required=True)
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()


protein_of_codon = json.load(args.codon)
rna_seq = args.dataset.read().strip()

protein_seq = ''
for triple in grouper(rna_seq, 3):
    codon = ''.join(triple)
    protein = protein_of_codon[codon]

    if protein == 'Stop':
        break
    else:
        protein_seq += protein

print (protein_seq)