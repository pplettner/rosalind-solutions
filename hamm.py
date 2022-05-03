#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

seq1 = args.dataset.readline().strip()
seq2 = args.dataset.readline().strip()

hamming_distance = 0

for (nucl1, nucl2) in zip(seq1, seq2):
    if nucl1 != nucl2:
        hamming_distance += 1

print (hamming_distance)