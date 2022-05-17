#!/usr/local/bin/python3

import argparse
from utils import read_fasta,reverse_complement

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

for (_, seq) in read_fasta(args.dataset):
    for start in range(len(seq)-3):
        for sublen in range(4, min(13, len(seq)-start+1)):
            if seq[start:start+sublen] == reverse_complement(seq[start:start+sublen]):
                print (start+1, sublen)
