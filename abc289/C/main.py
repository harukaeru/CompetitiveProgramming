#!/usr/bin/env python3.8
N,M=map(int, input().split())

s_list = []
for i in range(M):
  c = int(input())
  A = set(map(int, input().split()))
  s_list.append(A)


cnt = 0
for i in range(2 ** M):
  j = i
  ss = set()
  for k in range(M):
    if j % 2 == 1:
      ss = ss.union(s_list[k])
    j //= 2
  # print(ss)
  if len(ss) == N:
    cnt += 1

print(cnt)