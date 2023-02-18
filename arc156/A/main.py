#!/usr/bin/env python3.8
from bisect import bisect_left


T = int(input())
for i in range(T):
  N = int(input())
  S = list(input())
  K = []
  for i in range(N):
    if S[i] == '1':
      K.append(i)
  # print(K)
  if not K:
    print('0')
    continue

  k = K[0]
  idx = 0
  cnt = 0
  ng = False
  l = 0
  r = 0
  chosen = set()
  while idx < len(K):
    while idx in chosen and idx + 1 < len(K):
      idx += 1
      k = K[idx]

    # print('idx', idx)
    # print('k', k)
    # print('---')
    p = bisect_left(K, k + 2)
    # print('p', p)
    if p >= len(K):
      ng = True
      break

    while p in chosen or p == idx:
      p += 1
    chosen.add(p)
    # print(chosen)

    if p >= len(K):
      break
    # print('idx', (idx, p))
    # print('A', (K[idx], K[p]))

    if idx + 1 < p:
      idx = idx + 1
      k = K[idx]
    else:
      idx = p + 1
      k = K[p]
    cnt += 1
  if ng:
    print(-1)
  else:
    print(cnt)
  