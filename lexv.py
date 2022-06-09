#!/usr/local/bin/python3

import argparse
from itertools import product

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

alphabet = args.dataset.readline().split()
n = int(args.dataset.readline().strip())

cart_prods = []
for i in range(1,n+1):
    cart_prods.extend( [''.join(x) for x in product(alphabet, repeat=i)] )

sorted_prods = sorted(cart_prods, key=lambda x: [alphabet.index(c) for c in x])

print ('\n'.join(sorted_prods))