#!/usr/local/bin/python3
'''
By doing the Punnett squares, the probability that each generation will produce
an Aa (or Bb) genotype is always 1/2. Therefore p = 1/4 to get AaBb in each generation

We can reframe the problem as Bernoulli trials
(AaBb is a success, prob of success = p = 1/4, number of trials = n = 2^k)

That means the probability distribution is binomial
Prob mass function -> Pr(X=k) = (n choose k) * p^k * (1-p)^(n-k)

Cumulative distribution function -> Pr(X<=N-1) =
(2^k choose 1) * (1/4) * (3/4)^(2^k-1) + 
(2^k choose 2) * (1/4)^2 * (3/4)^(2^k-2) + ... +
(2^k choose N-1) * (1/4)^(N-1) * (3/4)^(2^k-N+1) + 

What we want is Pr(X>=N) = 1 - Pr(X<=N-1)
'''

import argparse
import math

def bernoulli_cdf(k, n, p):
    return sum(
        [math.comb(n,i) * math.pow(p,i) * math.pow(1-p,n-i) for i in range(k+1)]
    )

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

input_strings = args.dataset.readline().split(' ')
(k,N) = [int(x) for x in input_strings]

probability = 1 - bernoulli_cdf(N-1, pow(2,k), 0.25)

print (probability)