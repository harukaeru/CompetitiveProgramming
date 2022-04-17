#!/usr/bin/env python3
import itertools
S = input()

print(len(list(set(itertools.permutations(S)))))
