#!/usr/bin/env python3.8
import sys
sys.setrecursionlimit(300000)

H,W=map(int, input().split())
A = []
for i in range(H):
  x = list(input())
  A.append(x)

memo = {}
def dfs(y, x):
  if memo.get(y, {}).get(x):
    return memo[y][x]
  
  takahashi = (x + y) % 2
  if y == H - 1 and x == W - 1:
    memo.setdefault(y, {}).setdefault(x, 0)
    return 0

  if takahashi == 0:
    memo.setdefault(y, {}).setdefault(x, -1e18)
    if (y < H - 1):
      memo[y][x] = max(memo[y][x], dfs(y + 1, x) + (1 if A[y + 1][x] == '+' else -1))
    if (x < W - 1):
      memo[y][x] = max(memo[y][x], dfs(y, x + 1) + (1 if A[y][x + 1] == '+' else -1))
    return memo[y][x]
  else:
    memo.setdefault(y, {}).setdefault(x, 1e18)
    if (y < H - 1):
      memo[y][x] = min(memo[y][x], dfs(y + 1, x) + (-1 if A[y + 1][x] == '+' else 1))
    if (x < W - 1):
      memo[y][x] = min(memo[y][x], dfs(y, x + 1) + (-1 if A[y][x + 1] == '+' else 1))
    return memo[y][x]

ans = dfs(0, 0)
if ans > 0:
  print('Takahashi')
elif ans == 0:
  print('Draw')
else:
  print('Aoki')