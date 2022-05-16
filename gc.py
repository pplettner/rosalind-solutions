#!/usr/local/bin/python3

import argparse
from collections import Counter
from utils import read_fasta

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

max_gc_content = 0
max_gc_content_name = None

for (name, seq) in read_fasta(args.dataset):
    c = Counter(seq.upper())
    gc_content = (c['G'] + c['C'])/sum(c.values())

    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_content_name = name

print (max_gc_content_name)
print (max_gc_content * 100)