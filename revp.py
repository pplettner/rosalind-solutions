#!/usr/local/bin/python3

import argparse
from itertools import groupby

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

def reverse_complement(string):
    trans_table = str.maketrans('ACGT','TGCA')
    revc = string.upper()[::-1].translate(trans_table)
    return revc

parser = argparse.ArgumentParser()
parser.add_argument('dataset')
args = parser.parse_args()

for (name, seq) in read_fasta(args.dataset):
    for start in range(len(seq)-3):
        for sublen in range(4, min(13, len(seq)-start+1)):
            if seq[start:start+sublen] == reverse_complement(seq[start:start+sublen]):
                print (start+1, sublen)
