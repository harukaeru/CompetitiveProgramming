#!/usr/bin/env pypy3
from collections import Counter
import sys
sys.setrecursionlimit(300000)


S = input()

X = set()
X = [set() for i in range(len(S))]

used = set()

c = 0
i = 0
while i < len(S):
  # print(X)
  if S[i] == '(':
    c += 1
  elif S[i] == ')':
    used -= X[c]
    c -= 1
  else:
    if S[i] in used:
      print('No')
      exit()

    X[c].add(S[i])
    used.add(S[i])
    
  i += 1

print('Yes')