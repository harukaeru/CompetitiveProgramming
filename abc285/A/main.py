#!/usr/bin/env python3.8
import collections


G = collections.defaultdict(list)
A = [
  (1, 2),
  (1, 3),
  (2, 4),
  (2, 5),
  (3, 6),
  (3, 7),
  (4, 8),
  (4, 9),
  (5, 10),
  (5, 11),
  (6, 12),
  (6, 13),
  (7, 14),
  (7, 15),
]

for a in A:
  G[a[0]].append(a[1])
  G[a[1]].append(a[0])

a, b = map(int, input().split())

if b in G[a]:
  print('Yes')
else:
  print('No')