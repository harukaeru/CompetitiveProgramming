#!/usr/bin/env pypy3
from itertools import permutations

s1 = input()
s2 = input()
s3 = input()

s = set(s1).union(set(s2)).union(set(s3))
if len(s) > 10:
  print('UNSOLVABLE')
  exit()

s = list(s) + [''] * (10 - len(s))
def repl(s, d):
  r = 0
  l = len(s)
  k = 0
  p = 1
  while l > 0:
    t = d[s[l - 1 - k]]
    r += t * p
    p *= 10
    l -= 1
  if t == 0:
    return -1111111111111
  return r
for x in permutations(s):
  t1 = s1
  t2 = s2
  t3 = s3
  # print('x', x)
  d = dict()
  for i, v in enumerate(x):
    if not v:
      continue
    d[v] = i
  t1 = repl(t1, d)
  t2 = repl(t2, d)
  t3 = repl(t3, d)
  if t1 + t2 == t3:
    print(t1)
    print(t2)
    print(t3)
    exit()
print('UNSOLVABLE')