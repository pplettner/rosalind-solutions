#!/usr/local/bin/python3
'''
N1. AA-AA
N2. AA-Aa
N3. AA-aa
N4. Aa-Aa
N5. Aa-aa
N6. aa-aa

Expected count of dominant phenotype if each has 2 offspring:

2*[N1 + N2 + N3 + 3/4*N4 + 1/2*N5]
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

input_strings = args.dataset.readline().split(' ')
(N1,N2,N3,N4,N5,N6) = [int(x) for x in input_strings]

dominant_expectation = 2*(N1 + N2 + N3 + 0.75*N4 + 0.5*N5)

print (dominant_expectation)