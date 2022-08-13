#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))

dic = [0] * 2001

for a in A:
  dic[a] += 1

for i, d in enumerate(dic):
  if d == 0:
    print(i)
    exit()