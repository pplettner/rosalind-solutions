#!/usr/local/bin/python3

import argparse
from utils import reverse_complement

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

dna_string = args.dataset.readline().strip()
revc = reverse_complement(dna_string)

print (revc)