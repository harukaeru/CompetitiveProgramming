#!/usr/bin/env python3.8
N = int(input())
non_cheers = []
diffs = []
for i in range(N):
  a, b = map(int, input().split())
  non_cheers.append(-a)
  diffs.append(a + b + a)

nc = sum(non_cheers)
diffs.sort(reverse=True)

cnt = 0
for d in diffs:
  nc += d
  cnt += 1
  if nc > 0:
    print(cnt)
    exit()