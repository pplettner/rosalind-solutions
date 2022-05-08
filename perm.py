#!/usr/local/bin/python3

import argparse
from itertools import permutations

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

n = int(args.dataset.readline().strip())

perms = list(permutations(range(1,n+1), n))

print (len(perms))
for p in perms:
    print (' '.join([str(x) for x in p]))