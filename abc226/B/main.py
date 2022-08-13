#!/usr/bin/env python3
N = int(input())

ans_set = set()
for x in range(N):
  l, *a = map(int, input().split())
  a = tuple(a)
  ans_set.add(a)

print(len(ans_set))