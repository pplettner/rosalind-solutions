#!/usr/local/bin/python3
'''
Probability that a random sequence with GC content x produces the exact
input sequence S (P_s): solution in prob.py

If we're trying to find the input S as a substring in a random sequence 
R, there are length(R) - length(S) + 1 locations it could be.
( R[0:len(S)], R[1:len(S)+1], ... )

There the total expected number of times S occurs in R is the sum
of the probabilities of finding S at each possible location in R:

P_s + P_s + P_s + ... [length(R)-length(S)+1 times]
= P_s * (length(R)-length(S)+1)
'''

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

n = int(args.dataset.readline().strip())
seq = args.dataset.readline().strip()
gc_contents = [float(x) for x in args.dataset.readline().split()]

prob_functions = {
    'A' : lambda x: (1 - x)/2,
    'C' : lambda x: x/2,
    'G' : lambda x: x/2,
    'T' : lambda x: (1 - x)/2,
}

total_probs = []

for gc_content in gc_contents:
    prob_values = dict(
        (base, prob_functions[base](gc_content) ) for base in prob_functions.keys()
    )
    
    prob_s = math.prod([prob_values[base] for base in seq])
    total_probs.append(prob_s * (n-len(seq) + 1))
    
print (' '.join([str(x) for x in total_probs]))