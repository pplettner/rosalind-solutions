#!/usr/local/bin/python3

import argparse
from itertools import groupby
from collections import Counter

def read_fasta(filename):
    with open(filename) as f:
        fasta_iter = groupby(f, lambda line: line[0] == ">")

        for (is_header, val) in fasta_iter:
            val = [x.strip('\n>') for x in val]

            if is_header:
                [name] = val
            else:
                seq = ''.join(val)
                yield (name, seq)


parser = argparse.ArgumentParser()
parser.add_argument('dataset')
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