#!/usr/bin/env python3
import bisect
N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

D = [0] * (N + 1)
for i in range(1, N + 1):
  D[i] = D[i - 1] + A[i - 1]

def bfind(D, v):
  idx = bisect.bisect_left(D, v)
  if idx == len(D):
    return -1
  if D[idx] != v:
    return -1
  return idx

def find_candidates(val):
  candidates = {}
  for i in range(N):
    target = D[i] + val
    target_idx = bfind(D, target)
    if target_idx == -1:
      continue
    candidates[i] = target_idx
  return candidates

ps = find_candidates(P)
qs = find_candidates(Q)
rs = find_candidates(R)

for x, y in ps.items():
  if not qs.get(y):
    continue

  z = qs[y]
  if not rs.get(z):
    continue

  w = rs[z]
  # print(x, y, z, w)
  print('Yes')
  exit()

print('No')