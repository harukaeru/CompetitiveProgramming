#!/usr/bin/env python3.8
N = int(input())

anses = []
for i in range(3 ** N):
  p = i
  s = ''
  for j in range(N):
    if p % 3 == 0:
      s += 'a'
    elif p % 3 == 1:
      s += 'b'
    else:
      s += 'c'
    p //= 3
  anses.append(s)

anses.sort()
for a in anses:
  print(a)