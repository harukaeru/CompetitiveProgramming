#!/usr/bin/env python3.8
import sys
sys.setrecursionlimit(30000)

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
def dfs(rest, p1, p2, is_p1_turn):
  global cnt
  cnt += 1
  print('p', (p1, p2))
  if is_p1_turn:
    max_p1_score = -9999999999
    p2_score_when_max_p1 = -1
    for a in A:
      if rest < a:
        p1_score, p2_score = p1, p2
      else:
        next_p1 = p1 + a if is_p1_turn else p1
        p1_score, p2_score = dfs(rest - a, next_p1, p2, not is_p1_turn)
      if max_p1_score < p1_score:
        max_p1_score = p1_score
        p2_score_when_max_p1 = p2_score
    return max_p1_score, p2_score_when_max_p1
  else:
    max_p2_score = -9999999999
    p1_score_when_max_p2 = -1
    for a in A:
      if rest < a:
        p1_score, p2_score = p1, p2
      else:
        next_p2 = p2 + a if not is_p1_turn else p2
        p1_score, p2_score = dfs(rest - a, p1, next_p2, not is_p1_turn)
      if max_p2_score < p2_score:
        max_p2_score = p2_score
        p1_score_when_max_p2 = p1_score
    return p1_score_when_max_p2, max_p2_score

print(dfs(rest=N, p1=0, p2=0, is_p1_turn=True))
print('count', cnt)