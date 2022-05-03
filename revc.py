#!/usr/local/bin/python3

import argparse

def reverse_complement(string):
    trans_table = str.maketrans('ACGT','TGCA')
    revc = string.upper()[::-1].translate(trans_table)
    return revc

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

dna_string = args.dataset.readline().strip()
revc = reverse_complement(dna_string)

print (revc)