#!/usr/local/bin/python3
'''
Perfect matchings
---
AU:
= 1
AUAU:
2 U matches for 1st A, 1 U match for 2nd A
= 2*1
AUAUAU: 
3 U for 1st A, 2 U for 2nd A, 1 U for 3rd A
= 3*2*1

In general # perfect matchings = count(A)! [or count(U)!]

The same can be said for GC pairings, which are independent of AU pairings.

Therefore # perfect matchings = count(A)! * count(G)!
'''

import argparse
from collections import Counter
import math
from utils import read_fasta


parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

(_,seq) = next(read_fasta(args.dataset))

count = Counter(seq)
num_matchings = math.factorial(count['A']) * math.factorial(count['G'])

print (num_matchings)
