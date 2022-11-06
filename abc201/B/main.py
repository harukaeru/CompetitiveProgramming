#!/usr/bin/env python3.8
N = int(input())

tups = []
for i in range(N):
  name, h = input().split()
  h = int(h)
  tups.append((h, name))

tups.sort(reverse=True)

print(tups[1][1])