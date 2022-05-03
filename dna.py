#!/usr/local/bin/python3

import argparse
from collections import Counter

def count_dna_nucleotides(string):
    
    counter_dict = dict(Counter(string.upper()))
    return {k: counter_dict.get(k, 0) for k in ('A', 'C', 'G', 'T')}

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

dna_string = args.dataset.readline().strip()
dna_count = count_dna_nucleotides(dna_string)

print (' '.join([str(dna_count[k]) for k in ('A', 'C', 'G', 'T')]))