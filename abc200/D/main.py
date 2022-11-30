#!/usr/bin/env python3.8

from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

counter = defaultdict(list)
B = A[:8]
for i in range(2 ** len(B)):
  if i == 0:
    continue
  data = []
  vecs = []
  for j in range(len(B)):
    if i & (1 << j) != 0:
      vecs.append(B[j])
      data.append(j + 1)
  counter[sum(vecs) % 200].append(data)

for k, v in counter.items():
  if len(v) >= 2:
    print('Yes')
    v.sort()
    v[0].sort()
    v[1].sort()
    print(len(v[0]), *v[0])
    print(len(v[1]), *v[1])
    exit()

print('No')