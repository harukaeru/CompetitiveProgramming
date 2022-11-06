#!/usr/bin/env python3.8
N = int(input())
rang = [0] * (2 * (10 ** 5) + 1)
LR = []
for i in range(N):
  l, r = map(int, input().split())
  LR.append((l, r))
  rang[l] += 1
  rang[r] -= 1

for i in range(len(rang) - 1):
  rang[i + 1] += rang[i]

ans = []
current_l = 0
for i in range(len(rang)):
  if rang[i] != 0 and current_l == 0:
    current_l = i
  elif rang[i] == 0 and current_l != 0:
    ans.append((current_l, i))
    current_l = 0

for a in ans:
  print(*a)