#!/usr/local/bin/python3

import argparse
from utils import read_fasta

def reverse_complement(string):
    trans_table = str.maketrans('ACGT','TGCA')
    revc = string.upper()[::-1].translate(trans_table)
    return revc

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

for (name, seq) in read_fasta(args.dataset):
    for start in range(len(seq)-3):
        for sublen in range(4, min(13, len(seq)-start+1)):
            if seq[start:start+sublen] == reverse_complement(seq[start:start+sublen]):
                print (start+1, sublen)
