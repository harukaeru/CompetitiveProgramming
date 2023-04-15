#!/usr/bin/env python3.8
H,W=map(int, input().split())
S = []
for i in range(H):
  S.append(list(input()))

cnt = 0
for i in range(H):
  for j in range(W - 1):
    if S[i][j] == 'T' and S[i][j + 1] == 'T':
      S[i][j] = 'P'
      S[i][j + 1] = 'C'
      cnt += 1
for i in range(H):
  print(''.join(S[i]))