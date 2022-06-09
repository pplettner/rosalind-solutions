#!/usr/local/bin/python3
'''
Imagine the base case [unrooted binary tree]:

L - I - I - L
   /     \
  L       L

In this case you have:

Total nodes (N): 6
Total edges (E): 5 (= N-1 as discovered previously)
Leaves (L): 4
Internal nodes (I): 2

Growing this tree while keeping it unrooted binary requires that
you replace a leaf with an internal node and add 2 new leaves.

Each new iteration of the tree means that the net effect is 1 new 
internal node and 1 new leaf gets added each time.

Therefore I = L - 2 for all cases
'''

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

(n_leaves) = int(args.dataset.readline().strip())

print (n_leaves - 2)