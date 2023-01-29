#!/usr/bin/env python3.8
N,K=map(int, input().split())
A=list(map(int, input().split()))

l = -1
r = 10 ** 9 + 1

while r - l > 1:
  mid = (r + l) // 2
  cnt = 0
  for a in A:
    cnt += mid // a

  if cnt >= K:
    r = mid
  else:
    l = mid

print(r)