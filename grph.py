#!/usr/local/bin/python3

import argparse
from collections import defaultdict
from utils import read_fasta

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

names_of_prefix = defaultdict(set)
names_of_suffix = defaultdict(set)

for (name,seq) in read_fasta(args.dataset):
    prefix = seq[:3]
    suffix = seq[-3:]
    names_of_prefix[prefix].add(name)
    names_of_suffix[suffix].add(name)

for (suffix, suffix_names) in names_of_suffix.items():
    prefix_names = names_of_prefix.get(suffix, {})

    for s in suffix_names:
        for p in prefix_names:
            if s != p:
                print (s,p)