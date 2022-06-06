#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

n = int(args.dataset.readline().strip())
permutation = [int(x) for x in args.dataset.readline().split()]


inc = [(permutation[0],)] + [None] * (n-1)
max_inc = 1
inc_index = 0

dec = [(permutation[0],)] + [None] * (n-1)
max_dec = 1
dec_index = 0

for i in range(1,n):

    inc[i] = (permutation[i], )
    dec[i] = (permutation[i], )

    for prev in range(i):
        if permutation[prev] < permutation[i]:
            if len(inc[prev]) >= len(inc[i]):
                inc[i] = inc[prev] + (permutation[i], )

        if permutation[prev] > permutation[i]:
            if len(dec[prev]) >= len(dec[i]):
                dec[i] = dec[prev] + (permutation[i], )

    if len(inc[i]) > max_inc:
        max_inc = len(inc[i])
        inc_index = i

    if len(dec[i]) > max_dec:
        max_dec = len(dec[i])
        dec_index = i

print (' '.join([str(x) for x in inc[inc_index]]))
print (' '.join([str(x) for x in dec[dec_index]]))