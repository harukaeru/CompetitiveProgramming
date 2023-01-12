#!/usr/bin/env python3.8
N,K= map(int, input().split())
S = []
for i in range(N):
  s = int(input())
  S.append(s)
  if s == 0:
    print(N)
    exit()

l = 0
r = 0
cur = 1
used = False
m = 0
while l < N:
  # print('cur', cur)
  while r < N and cur * S[r] <= K:
    used = True
    cur *= S[r]
    r += 1

  # print(l, r, cur)
  if used and cur <= K:
    m = max(m, r - l)

  if used:
    cur //= S[l]
  if l == r:
    r += 1
  l += 1
print(m)