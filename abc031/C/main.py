#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

max_t_score = -1e18
for i in range(N):
  max_a_score = -1e18
  t_score_when_a_score_is_max = -1e18
  for j in range(N):
    t_score = 0
    a_score = 0

    if j == i:
      continue

    l = min(i, j)
    r = max(i, j)
    for kidx, k in enumerate(range(l, r + 1)):
      if kidx % 2 == 0:
        t_score += A[k]
      else:
        a_score += A[k]

    if max_a_score < a_score:
      max_a_score = a_score
      t_score_when_a_score_is_max = t_score
    
  max_t_score = max(max_t_score, t_score_when_a_score_is_max)

print(max_t_score)