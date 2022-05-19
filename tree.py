#!/usr/local/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

n = int(args.dataset.readline().strip())

subtrees = []
nodes = set()

for edge in args.dataset:
    (a,b) = [int(x) for x in edge.split()]

    a_index = None
    b_index = None

    for (i, subtree) in enumerate(subtrees):
        if a in subtree:
            a_index = i
        if b in subtree:
            b_index = i

    if a_index is None and b_index is None:
        subtrees.append({a,b})
    elif a_index is None:
        subtrees[b_index].add(a)
    elif b_index is None:
        subtrees[a_index].add(b)
    else:
        subtrees[b_index] |= subtrees[a_index]
        del subtrees[a_index]

    nodes |= {a,b}

edges_to_add = (n-len(nodes)) + (len(subtrees)-1)
print (edges_to_add)

