#!/usr/bin/env python3.8
N, M = map(int, input().split())
conditions = []
for i in range(M):
  a, b = map(int, input().split())
  conditions.append((a, b))

K = int(input())
commands = []
for i in range(K):
  c, d = map(int, input().split())
  commands.append((c, d))


max_match_cond = 0
for i in range(2 ** K):
  result = [0] * N
  j = i
  for k in range(K):
    pos = commands[k][j % 2]  
    result[pos - 1] += 1
    j //= 2

  match_cond = 0
  for cond in conditions:
    a, b = cond
    if result[a - 1] >= 1 and result[b - 1] >= 1:
      match_cond += 1
  max_match_cond = max(max_match_cond, match_cond)

print(max_match_cond)