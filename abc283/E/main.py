#!/usr/bin/env pypy3
from random import random


H, W = map(int, input().split())
A = []
AA = []
for i in range(H):
  B = list(map(int, input().split()))
  A.append(B)
  BB = B[:]
  AA.append(BB)


def inverse(s):
  return [1 - x for x in s]

cnt = 0
for i in range(H):
  found = False
  for j in range(W):
    ok = False
    for h, w in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if 0 <= i + h < H and 0 <= j+w < W:
          if A[i][j] == A[i + h][j + w]:
            ok = True
    if not ok:
        found = True
  if found:
    cnt += 1
    A[i] = inverse(A[i])
  # print('-------')
  # for a in A:
  #   print(a)

rcnt = 0
AA.reverse()
hh = random.shuffle((range(len(H))))
for i in hh :
  found = False
  for j in range(W):
    ok = False
    for h, w in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if 0 <= i + h < H and 0 <= j+w < W:
          if AA[i][j] == AA[i + h][j + w]:
            ok = True
    if not ok:
        found = True
  if found:
    rcnt += 1
    AA[i] = inverse(AA[i])

for i in range(H):
  found = False
  for j in range(W):
    ok = False
    for h, w in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if 0 <= i + h < H and 0 <= j+w < W:
          if A[i][j] == A[i + h][j + w]:
            ok = True
    if not ok:
        found = True
  if found:
    print(-1)
    exit()
print(min(cnt, rcnt))