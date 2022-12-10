#!/usr/bin/env python3.8
N = int(input())
S = list(input())

r = N - 1

cnt = 0
for l in range(N):
  if S[l] == 'R':
    continue

  while r > l:
    if S[r] == 'R':
      S[l], S[r] = S[r], S[l]
      cnt += 1
      break
    r -= 1

# print(S)
print(cnt)