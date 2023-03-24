#!/usr/bin/env python3.8
N,D,K=map(int, input().split())
days = []
for i in range(D):
  l,r=map(int, input().split())
  days.append((l, r))

nations = []
for i in range(K):
  s,t=map(int, input().split())
  nations.append([s,t])

for k in range(K):
  s, t = nations[k]
  ls = s
  rs = s
  for cnt, (l, r) in enumerate(days, 1):
    if l <= ls <= r:
      ls = l
    if l <= rs <= r:
      rs = r
    if ls <= t <= rs:
      # print((ls, rs))
      print(cnt)
      break
