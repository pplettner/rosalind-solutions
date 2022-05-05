#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

input_strings = args.dataset.readline().split(' ')
(n,m) = [int(x) for x in input_strings]

age_total = [1] + [0] * (m-1)

for i in range(1,n):
    age_total = [sum(age_total[1:])] + age_total[:-1]

print (sum(age_total))