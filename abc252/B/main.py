#!/usr/bin/env python3.8
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(list(map(int, input().split())))

max_a = max(A)
p = []
for i, a in enumerate(A):
  if max_a == a:
    p.append(i + 1)

for pp in p:
  if pp in B:
    print('Yes')
    exit()
print('No')