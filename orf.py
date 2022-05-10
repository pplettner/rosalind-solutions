#!/usr/local/bin/python3

import argparse
import json
from itertools import groupby,zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

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

def dna_to_rna(string):
    trans_table = str.maketrans('T','U')
    rna_string = string.upper().translate(trans_table)
    return rna_string

def rna_to_prot(seq, protein_of_codon):
    start = 0
    protein_seqs = []

    while (location := seq.find('AUG', start)) != -1:
        start = location + 3
        protein_seq = ''

        for triple in grouper(seq[location:], 3):
            if None in triple:
                break

            codon = ''.join(triple)
            protein = protein_of_codon[codon]

            if protein == 'Stop':
                protein_seqs.append(protein_seq)
                break
            else:
                protein_seq += protein

    return protein_seqs

def reverse_complement(string):
    trans_table = str.maketrans('ACGT','TGCA')
    revc = string.upper()[::-1].translate(trans_table)
    return revc


parser = argparse.ArgumentParser()
parser.add_argument('-c','--codon', help='Codon mapping json', type=argparse.FileType('r'), required=True)
parser.add_argument('dataset')
args = parser.parse_args()

(name, seq) = next(read_fasta(args.dataset))
protein_of_codon = json.load(args.codon)

rna_seq = dna_to_rna(seq)
revc_rna_seq = dna_to_rna(reverse_complement(seq))

candidates = set()

for s in (rna_seq, revc_rna_seq):
    candidates.update(rna_to_prot(s, protein_of_codon))

print ('\n'.join(candidates))