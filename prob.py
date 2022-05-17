#!/usr/local/bin/python3

import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

seq = args.dataset.readline().strip()
gc_contents = [float(x) for x in args.dataset.readline().split()]

prob_functions = {
    'A' : lambda x: (1 - x)/2,
    'C' : lambda x: x/2,
    'G' : lambda x: x/2,
    'T' : lambda x: (1 - x)/2,
}

total_log_prob = []

for gc_content in gc_contents:
    prob_values = dict(
        (base, prob_functions[base](gc_content) ) for base in prob_functions.keys()
    )
    total_log_prob.append(sum([math.log10(prob_values[base]) for base in seq]))

print (' '.join([str(x) for x in total_log_prob]))