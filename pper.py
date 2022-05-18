#!/usr/local/bin/python3
'''
Permutations of k items from N: P(N,k) = N! / (N-k)!
More explicitly, P(N,k) = N * (N-1) * ... (N-k+1)

One liner solution: math.perm(n,k) % 1000000

Solution below is more in the spirit of the question, not storing
the whole product value in the variable but just the modulo value
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

(n,k) = [int(x) for x in args.dataset.readline().split()]

perms = 1
for i in range(k):
    perms *= (n-i)
    perms %= 1000000

print (perms)