#!/usr/bin/env python3.8
import itertools


N = int(input())
A = list(map(int, input().split()))
B = [0] + list(itertools.accumulate(A))
Q = int(input())
for i in range(Q):
  l,r=map(int, input().split())
  ok_cnt = B[r] - B[l - 1]
  tot = (r - l + 1)
  ng_cnt = tot - ok_cnt
  if ok_cnt > ng_cnt:
    print('win')
  elif ok_cnt == ng_cnt:
    print('draw')
  else:
    print('lose')