#!/usr/local/bin/python3

import argparse
from utils import rna_to_prot

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

rna_seq = args.dataset.read().strip()
protein_seq = rna_to_prot(rna_seq)
print (protein_seq)