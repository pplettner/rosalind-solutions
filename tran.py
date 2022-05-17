#!/usr/local/bin/python3

import argparse
from utils import read_fasta

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

(name1, seq1) = next(read_fasta(args.dataset))
(name2, seq2) = next(read_fasta(args.dataset))

transitions = 0
transversions = 0

for (nucl1, nucl2) in zip(seq1, seq2):
    nucl_set = {nucl1, nucl2}

    if nucl_set == {'A','G'} or nucl_set == {'C','T'}:
        transitions += 1
    elif len(nucl_set) == 2:
        transversions += 1

print (transitions/transversions)
        
        
