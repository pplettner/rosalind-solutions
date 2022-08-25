#!/usr/local/bin/python3

import argparse
from collections import defaultdict
from itertools import product
from utils import read_fasta

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

(_,seq) = next(read_fasta(args.dataset))

kmer_count = defaultdict(int)

for i in range(0,len(seq)-4+1):
    kmer_count[seq[i:i+4]] += 1

kmers = [''.join(x) for x in product('ACGT', repeat=4)]

print (' '.join([str(kmer_count.get(kmer,0)) for kmer in kmers]))  