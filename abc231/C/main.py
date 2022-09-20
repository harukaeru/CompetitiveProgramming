#!/usr/bin/env python3
import bisect
N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
def get_ans(x):
  pos = bisect.bisect_left(A, x)
  return len(A) - pos

for i in range(Q):
  x = int(input())
  print(get_ans(x))