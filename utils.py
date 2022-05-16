from importlib.resources import read_text
from itertools import groupby, zip_longest
import json

PROTEIN_OF_CODON = json.loads(
    read_text('data', 'rna_codon.json')
)

def read_fasta(handle):
    fasta_iter = groupby(handle, lambda line: line[0] == ">")

    for (is_header, val) in fasta_iter:
        val = [x.strip('\n') for x in val]

        if is_header:
            [name] = val
            # Return name without ">" prefix
            name = name[1:]
        else:
            seq = ''.join(val)
            yield (name, seq)

def rna_to_prot(seq):
    protein_seq = ''

    for triple in grouper(seq, 3):
        if None in triple:
            break
        codon = ''.join(triple)
        protein = PROTEIN_OF_CODON[codon]

        if protein == 'Stop':
            break
        else:
            protein_seq += protein

    return protein_seq

# Collect data into fixed-length chunks or blocks
#
# Taken from Python docs: Itertools Recipes
# https://docs.python.org/3/library/itertools.html

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)