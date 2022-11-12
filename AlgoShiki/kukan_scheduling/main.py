#!/usr/bin/env python3.8
N = int(input())
ST = []
for i in range(N):
  s, t = map(int, input().split())
  ST.append((s, t))

ST.sort(key=lambda x: (x[1], x[0]))

cnt = 0
m = 0
for i in range(N):
  s, t = ST[i]
  if s < m:
    continue

  m = t
  cnt += 1

print(cnt)
