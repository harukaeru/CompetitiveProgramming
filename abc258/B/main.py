#!/usr/bin/env python3
N = int(input())
A = []
for i in range(N):
  a = [int(s) for s in input()]
  A.append(a)

print(A)

def dfs(i, j, loop, path=[], memory=set()):
  path = path + [A[i][j]]
  memory = memory.union(set([(i, j)]))

  if loop == 1:
    return path

  left = i - 1 if i - 1 >= 0 else N - 1
  right = i + 1 if i + 1 < N else 0
  below = j + 1 if j + 1 < N else 0
  above = j - 1 if j - 1 >= 0 else N - 1

  ret_paths = []
  if (left, j) not in memory:
    ret_paths.append(dfs(left, j, loop - 1, path, memory))
  if (right, j) not in memory:
    ret_paths.append(dfs(right, j, loop - 1, path, memory))
  if (i, below) not in memory:
    ret_paths.append(dfs(i, below, loop - 1, path, memory))
  if (i, above) not in memory:
    ret_paths.append(dfs(i, above, loop - 1, path, memory))
  if (left, below) not in memory:
    ret_paths.append(dfs(left, below, loop - 1, path, memory))
  if (left, above) not in memory:
    ret_paths.append(dfs(left, above, loop - 1, path, memory))
  if (right, below) not in memory:
    ret_paths.append(dfs(right, below, loop - 1, path, memory))
  if (right, above) not in memory:
    ret_paths.append(dfs(right, above, loop - 1, path, memory))

  return max(ret_paths) if ret_paths else []

for i in range(N):
  for j in range(N):
    print(dfs(i, j, N))