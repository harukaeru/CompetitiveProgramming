#!/usr/bin/env python3.8
@profile
def main():
  from queue import deque
  N = int(input())
  A = []
  for i in range(N):
    a = [s for s in input()]
    A.append(a)
  
  @profile
  def bfs(i, j, N):
    q = deque()
    seen = set()
    seen.add((i, j))
    q.append((i, j, '', seen))
  
    max_s = '0'
    while len(q) > 0:
      ti, tj, s, seen = q.popleft()
  
      s += A[ti][tj]
      if len(s) == N:
        max_s = max(max_s, s)
        continue
  
      left = (ti - 1) % N
      right = (ti + 1) % N
      above = (tj - 1) % N
      below = (tj + 1) % N
      for x in [left, ti, right]:
        for y in [above, tj, below]:
          if x == ti and y == tj:
            continue
          if (x, y) not in seen:
            q.append((x, y, s, seen.union([(x, y)])))
      
    return max_s
  
  max_s = '0'
  for i in range(N):
    for j in range(N):
      s = bfs(i, j, N)
      max_s = max(max_s, s)
      break
  
  
  
  print(max_s)