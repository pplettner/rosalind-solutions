#!/usr/local/bin/python3

import argparse
from itertools import groupby

def read_fasta(filename):
    with open(filename) as f:
        fasta_iter = groupby(f, lambda line: line[0] == ">")

        for (is_header, val) in fasta_iter:
            val = [x.strip('\n>') for x in val]

            if is_header:
                [name] = val
            else:
                seq = ''.join(val)
                yield (name, seq)

# Calculating LCS of N arbitrary strings by:
# - Binary search of possible substring lengths of first string
# - For each length, check every substring in all other input strings

# TODO: Rewrite using suffix trees

def lcs(*seqs):
    lc_strs = {''}
    reference_str = seqs[0]

    min_len = 0
    max_len = len(reference_str) + 1


    while max_len > min_len + 1:
        candidate_len = int((max_len + min_len) / 2)
        candidates = set()

        for i in range(len(reference_str) - candidate_len + 1):
            candidate = reference_str[i:i+candidate_len]

            if all(candidate in seq for seq in seqs):
                candidates.add(candidate)

        if len(candidates) > 0:
            lc_strs = candidates
            min_len = candidate_len
        else:
            max_len = candidate_len

    return (lc_strs)

parser = argparse.ArgumentParser()
parser.add_argument('dataset')
args = parser.parse_args()


all_seqs = [seq for (name,seq) in read_fasta(args.dataset)]

# Print arbitrary result instead of all of them
print (lcs(*all_seqs).pop())