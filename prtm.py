#!/usr/local/bin/python3

import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mass', help='Amino acid mass json', type=argparse.FileType('r'), required=True)
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()


mass_of_aa = json.load(args.mass)
prot_seq = args.dataset.read().strip()

total_mass = sum([mass_of_aa[prot] for prot in prot_seq])
print (total_mass)