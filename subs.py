#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

seq1 = args.dataset.readline().strip()
seq2 = args.dataset.readline().strip()

start = 0
locations = []

while (location := seq1.find(seq2, start)) != -1:
    locations.append(location + 1)
    start = location + 1

print (' '.join([str(x) for x in locations]))