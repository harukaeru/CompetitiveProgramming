#!/usr/bin/env python3
N, M = map(int, input().split())

A = []

def dfs(s):
  if len(A) == N:
    print(' '.join(map(str, A)))
    return

  for j in range(s + 1, M + 1):
    A.append(j)
    dfs(j)
    A.pop()

dfs(0)