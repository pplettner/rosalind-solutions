#!/usr/local/bin/python3

import argparse
from itertools import product

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

alphabet = args.dataset.readline().split()
n = int(args.dataset.readline().strip())

cart_prod = product(alphabet, repeat=n)

for p in cart_prod:
    print (''.join([str(x) for x in p]))