#!/usr/local/bin/python3

import argparse
from collections import Counter,defaultdict
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

parser = argparse.ArgumentParser()
parser.add_argument('dataset')
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