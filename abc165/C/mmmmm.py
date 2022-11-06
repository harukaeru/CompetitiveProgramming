#!/usr/bin/env python3.8
N, M, Q = map(int, input().split())

N = 7
M = 7
A = [1] * N

def dfs(current = 0, dest = 1, depth=0):
  print('  ' * depth, dest)
  if current == N:
    print(A)
    return
  
  for v in range(dest, M + 1, 2):
    A[current] = v
    dfs(current + 1, v, depth+1)
  
    
dfs()