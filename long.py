#!/usr/local/bin/python3

import argparse
from itertools import permutations
from utils import read_fasta

def overlap_position(seq1, seq2):
    '''
    Determines whether the end of s1 overlaps with the start of s2.
    It requires that the overlap length be >1/2 of the total string length.
    '''
    mid = int( len(seq2)/2 ) + 1
    start = seq1.find(seq2[:mid])

    if start != -1:
        chars_left = len(seq1) - mid - start
        if seq1[-chars_left:] == seq2[mid:mid+chars_left]:
            return mid+chars_left

    return 0

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

input_seqs = [seq for (_,seq) in read_fasta(args.dataset)]
best_overlap = dict()

for (seq1, seq2) in permutations(input_seqs,2):
    if seq1 not in best_overlap:
        pos = overlap_position(seq1, seq2)
        if pos > 0:
            best_overlap[seq1] = (seq2, pos)


(first_seq,) = set(input_seqs) - set([x[0] for x in best_overlap.values()])
consensus = seq = first_seq

while (overlap := best_overlap.get(seq)) is not None:    
    successor = overlap[0]
    pos = overlap[1]
    consensus += successor[pos:]
    seq = successor

print (consensus)

