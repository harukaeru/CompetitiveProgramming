#!/usr/bin/env python3.8
N = int(input())
S = input()

def add_vec(a, b):
  return (a[0] + b[0], a[1] + b[1])

seen = set()
s = (0, 0)
seen.add(s)
for dr in S:
  if dr == 'R':
    nex = add_vec(s, (1, 0))
  elif dr == 'L':
    nex = add_vec(s, (-1, 0))
  elif dr == 'U':
    nex = add_vec(s, (0, 1))
  elif dr == 'D':
    nex = add_vec(s, (0, -1))
  if nex in seen:
    print('Yes')
    exit()

  seen.add(nex)
  s = nex
print('No')