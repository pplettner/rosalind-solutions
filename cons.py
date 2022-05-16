#!/usr/local/bin/python3

import argparse
from collections import Counter,defaultdict
from utils import read_fasta

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

all_seqs = [seq for (name,seq) in read_fasta(args.dataset)]

profile_matrix = defaultdict(list)
consensus = ''

for base_tuple in zip(*all_seqs):
    counter = Counter(base_tuple)
    [(consensus_base, count)] = counter.most_common(1)
    consensus += consensus_base

    for base in 'ACGT':
        profile_matrix[base].append(counter[base])

print (consensus)

for base in 'ACGT':
    print (f'{base}: ' + ' '.join([str(x) for x in profile_matrix[base]]))