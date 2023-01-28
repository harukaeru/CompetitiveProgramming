#!/usr/bin/env python3.8
N = int(input())
cnt = 0
p = 0
for i in range(N):
  S = input()
  if S == 'For':
    cnt += 1
  else:
    p += 1

if cnt >= p:
  print('Yes')
else:
  print('No')