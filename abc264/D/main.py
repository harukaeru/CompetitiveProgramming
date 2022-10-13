#!/usr/bin/env python3
S = list(input())

def count(S, x):
  c = S.index(x)
  S.remove(x)
  return c

t = 0
for s in 'atcoder':
  t += count(S, s)

print(t)