#!/usr/local/bin/python3

import argparse

def dna_to_rna(string):
    trans_table = str.maketrans('T','U')
    rna_string = string.upper().translate(trans_table)
    return rna_string

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

dna_string = args.dataset.readline().strip()
rna_string = dna_to_rna(dna_string)

print (rna_string)