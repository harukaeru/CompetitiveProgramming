#!/usr/bin/env python3
N, S = map(int, input().split())

cnt = 0
for i in range(1, N + 1):
  anc = S - i
  if anc > 0:
    cnt += min(N, anc)
print(cnt)

  # for j in range(1, N + 1):
  #   if i + j <= S:
  #     cnt += 1
