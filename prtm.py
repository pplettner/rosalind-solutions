#!/usr/local/bin/python3

import argparse
from utils import MASS_OF_AA

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

prot_seq = args.dataset.read().strip()

total_mass = sum([MASS_OF_AA[prot] for prot in prot_seq])
print (total_mass)