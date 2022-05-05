#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

input_strings = args.dataset.readline().split(' ')
(n,k) = [int(x) for x in input_strings]

prev = 1
total = 1

for i in range(2,n):
    prev, total = total, k*prev + total

print (total)