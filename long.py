#!/usr/local/bin/python3

import argparse
from itertools import permutations
from utils import read_fasta

def overlap_position(s1,s2):
    '''
    Determines whether the end of s1 overlaps with the start of s2.
    It requires that the overlap length be >1/2 of the total string length.
    '''
    mid = int( len(s2)/2 ) + 1
    start = s1.find(s2[:mid])

    if start != -1:
        chars_left = len(s1) - mid - start
        if s1[-chars_left:] == s2[mid:mid+chars_left]:
            return mid+chars_left

    return 0

    
parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

input_seqs = [seq for (_,seq) in read_fasta(args.dataset)]
next_seq = dict()
overlap_pos = dict()

for (a,b) in permutations(input_seqs,2):
    if a not in next_seq:
        i = overlap_position(a,b)
        if i > 0:
            next_seq[a] = b
            overlap_pos[a] = i


(first_seq,) = set(input_seqs) - set(next_seq.values())
consensus = curr = first_seq

while (successor := next_seq.get(curr)) is not None:    
    i = overlap_pos[curr]
    consensus += successor[i:]

    curr = successor

print (consensus)
