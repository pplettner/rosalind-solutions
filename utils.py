from importlib.resources import read_text
from itertools import groupby, zip_longest
import json

PROTEIN_OF_CODON = json.loads(
    read_text('data', 'rna_codon.json')
)

MASS_OF_AA = json.loads(
    read_text('data', 'aa_mass.json')
)

class InvalidSequenceException(Exception):
    """Exception raised for errors in the RNA->protein transcription
    """

    def __init__(self, message):
        super().__init__(message)


def dna_to_rna(string):
    return string.upper().replace('T','U')

def reverse_complement(string):
    trans_table = str.maketrans('ACGT','TGCA')
    revc = string.upper()[::-1].translate(trans_table)
    return revc


def read_fasta(handle):
    fasta_iter = groupby(handle, lambda line: line[0] == ">")
    name = None
    seq = None
    
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
    start_found = False
    stop_found = False

    for triple in grouper(seq, 3):
        if None in triple:
            codon = ''.join([x for x in triple if x is not None])
            raise InvalidSequenceException(f"Sequence truncated (ended with {codon})")

        codon = ''.join(triple)

        try:
            protein = PROTEIN_OF_CODON[codon]
        except KeyError:
            raise InvalidSequenceException(f"Codon {codon} not found in lookup table")

        if start_found:
            if protein == 'Stop':
                stop_found = True
                break
            else:
                protein_seq += protein
        elif codon == 'AUG':
            start_found = True
            protein_seq = protein

    if not stop_found:
        raise InvalidSequenceException("Sequence doesn't end with stop codon")

    return protein_seq

# Collect data into fixed-length chunks or blocks
#
# Taken from Python docs: Itertools Recipes
# https://docs.python.org/3/library/itertools.html

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)