#!/usr/local/bin/python3
'''
To construct an arbitary subset of a given set, you can look at
each set element and assign it as being IN or OUT of the subset.

So you can construct all subsets by counting how many combinations
of IN/OUT there are over the number of set elements (=N), which is:

2 * 2 * 2... N times = 2^N
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

(n) = int(args.dataset.readline().strip())

num_subsets = 1

for i in range(n):
    num_subsets = (num_subsets * 2) % 1000000

print (num_subsets)
