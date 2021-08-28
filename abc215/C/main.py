#!/usr/bin/env python3
import itertools

S, K = input().split()

S = [s for s in S]
S.sort()

K = int(K)

S_permutationed = list(itertools.permutations(S))
S_permutationed = [''.join(s) for s in S_permutationed]
S_permutationed = sorted(set(S_permutationed))

print(''.join(S_permutationed[K - 1]))
