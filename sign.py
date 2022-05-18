#!/usr/local/bin/python3

import argparse
from itertools import combinations,permutations

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

n = int(args.dataset.readline().strip())

perms = list(permutations(range(1,n+1), n))

index_combos = []
for i in range(1,n+1):
    index_combos.extend(combinations(range(n), i))

print ( len(perms) * (len(index_combos) + 1) )

for p in perms:
    print (' '.join([str(x) for x in p]))

    for ic in index_combos:
        signed_perm = list(p)
        for i in ic:
            signed_perm[i] *= -1

        print (' '.join([str(x) for x in signed_perm]))