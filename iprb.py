#!/usr/local/bin/python3
'''
k = homozygous dominant
m = heterozygous
n = homozygous recessive
t = k + m + n

p(1=k, 2=k) = (k/t) * (k-1)/(t-1) -- dominant
p(1=k, 2=m) = (k/t) * m/(t-1)     -- dominant
p(1=k, 2=n) = (k/t) * n/(t-1)     -- dominant

p(1=m, 2=k) = (m/t) * k/(t-1)     -- dominant
p(1=m, 2=m) = (m/t) * (m-1)/(t-1) -- 3/4 dom, 1/4 rec
p(1=m, 2=n) = (m/t) * n/(t-1)     -- 1/2 dom, 1/2 rec

p(1=n, 2=k) = (n/t) * k/(t-1)     -- dominant
p(1=n, 2=m) = (n/t) * m/(t-1)     -- 1/2 dom, 1/2 rec
p(1=n, 2=n) = (n/t) * (n-1)/(t-1) -- recessive
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

input_strings = args.dataset.readline().split(' ')
(k,m,n) = [int(x) for x in input_strings]
t = k + m + n

probability_recessive = \
    (n/t) * (n-1)/(t-1) + \
    (n/t) * m/(t-1) + \
    0.25 * (m/t) * (m-1)/(t-1)
    
probability_dominant = 1 - probability_recessive

print (probability_dominant)