#!/usr/bin/env python3.8
X = input()
N = int(input())

S = []
for i in range(N):
    word = input()
    S.append(word)
al = 'abcdefghijklmnopqrstuvwxyz'

replacer = {}
for i, a in enumerate(al):
    replacer[X[i]] = a


def func(w):
    nw = ''
    for l in w:
        nw += replacer[l]
    return nw

for ss in sorted(S, key=func):
    print(ss)
