#!/usr/local/bin/python3

import argparse
from itertools import combinations
from utils import read_fasta

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

input_seqs = [seq for (_,seq) in read_fasta(args.dataset)]
num_seqs = len(input_seqs)


distance_matrix = [ [0.0] * num_seqs for i in range(num_seqs) ] 

for (i1, i2) in combinations(range(num_seqs), 2):
    hamming_distance = 0

    for (nucl1, nucl2) in zip(input_seqs[i1], input_seqs[i2]):
        if nucl1 != nucl2:
            hamming_distance += 1

    p_distance = hamming_distance / len(input_seqs[i1])

    distance_matrix[i1][i2] = p_distance
    distance_matrix[i2][i1] = p_distance


for i in range(num_seqs):
    print (' '.join([str(x) for x in distance_matrix[i]]))