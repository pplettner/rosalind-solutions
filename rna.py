#!/usr/local/bin/python3

import argparse
from utils import dna_to_rna

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

dna_string = args.dataset.readline().strip()
rna_string = dna_to_rna(dna_string)

print (rna_string)