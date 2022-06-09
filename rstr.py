#!/usr/local/bin/python3
'''
Probability that a random sequence with GC content x produces the exact
input sequence (P_s): solution in prob.py

Probability that 0 of N candidate sequences are the input: (1-P_s)^N

Probability that 1 or more candidates are the input: 1 - ( (1-P_s)^N )
'''

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

(n, gc_content) = args.dataset.readline().split()
seq = args.dataset.readline().strip()

n = int(n)
gc_content = float(gc_content)

prob_functions = {
    'A' : lambda x: (1 - x)/2,
    'C' : lambda x: x/2,
    'G' : lambda x: x/2,
    'T' : lambda x: (1 - x)/2,
}

prob_values = dict(
    (base, prob_functions[base](gc_content) ) for base in prob_functions.keys()
)

prob_s = math.prod([prob_values[base] for base in seq])
prob = 1 - (math.pow(1-prob_s, n))

print (prob)