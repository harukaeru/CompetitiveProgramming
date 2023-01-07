#!/usr/bin/env python3.8
N = int(input())

cache = []
for i in range(10):
  p = [0] * 10
  cache.append(p)

for i in range(1, N + 1):
  s = str(i)
  f = ord(s[0]) - ord('0')
  l = ord(s[-1]) - ord('0')
  if f == 0 or l == 0:
    continue

  cache[f][l] += 1

tot = 0
for i in range(1, 10):
  for j in range(1, 10):
    tot += cache[i][j] * cache[j][i]
print(tot)