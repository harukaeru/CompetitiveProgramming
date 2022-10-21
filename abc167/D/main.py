#!/usr/bin/env python3
N, K = map(int, input().split())
A = list(map(int, input().split()))

pos = {}
dests = []
det_pos = -1
next_city = 1

for i in range(N):
  if pos.get(next_city) is not None:
    det_pos = pos[next_city]
    break

  dests.append(next_city)
  pos[next_city] = i
  next_city = A[next_city - 1]

if det_pos >= K:
  print(dests[K])
  exit()

m = (K - det_pos) % (len(dests) - det_pos)
print(dests[det_pos + m])