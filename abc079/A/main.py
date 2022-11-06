#!/usr/bin/env python3.8
N = input()

for p in [s * 3 for s in set(N)]:
  if p in N:
    print('Yes')
    exit()
print('No')