#!/usr/local/bin/python3

import argparse
from utils import read_fasta

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

fa_iter = read_fasta(args.dataset)

(_, seq) = next(fa_iter)
(_, subseq) = next(fa_iter)

base_locations = []
start = 0

for base in subseq:
    base_location = seq.find(base, start)
    base_locations.append(base_location + 1)
    start = base_location + 1

print (' '.join([str(x) for x in base_locations]))