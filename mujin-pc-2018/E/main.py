#!/usr/bin/env python3.8
from bisect import bisect_left
import heapq

N,M,K=map(int, input().split())
d = list(input())
S = []
for i in range(N):
  S.append(input())

ups = [i for i in range(K) if d[i] == 'U']
downs = [i for i in range(K) if d[i] == 'D']
lefts = [i for i in range(K) if d[i] == 'L']
rights = [i for i in range(K) if d[i] == 'R']

def get_t(s, cache):
  if not cache:
    return None
  pos = bisect_left(cache, s)
  if pos >= len(cache):
    pos = 0
    return cache[pos] + K
  return cache[pos]

def calc_cost(s, nex_time):
  if nex_time is None:
    return 1e18
  nex = nex_time + 1
  return nex - s

def get_cost(s):
  up = get_t(s, ups)
  down = get_t(s, downs)
  left = get_t(s, lefts)
  right = get_t(s, rights)
  return list(map(lambda nex: calc_cost(s, nex), [up, right, down, left]))

costs = []
for i in range(K):
  cost = get_cost(i)
  costs.append(cost)

dp = []
for i in range(N):
  dp.append([1e18] * M)

s = None
goal = None
for i in range(N):
  for j in range(M):
    if S[i][j] == 'S':
      s = (i, j)
    elif S[i][j] == 'G':
      goal = (i, j)
      

pq = [(0, s)]
dp[s[0]][s[1]] = 0

directions = {
  0: (-1, 0),
  1: (0, 1),
  2: (1, 0),
  3: (0, -1),
}
while pq:
  c, v = heapq.heappop(pq)
  y, x = v
  if dp[y][x] < c:
    continue

  for orientation, (dy, dx) in directions.items():
    if y + dy < 0 or y + dy >= N:
      continue
    if x + dx < 0 or x + dx >= M:
      continue
    if S[y + dy][x + dx] == '#':
      continue

    candidate_cost = dp[y][x] + costs[c % K][orientation]
    if dp[y + dy][x + dx] > candidate_cost:
      dp[y + dy][x + dx] = candidate_cost
      heapq.heappush(pq, (candidate_cost, (y + dy, x + dx)))

ans = dp[goal[0]][goal[1]]
if ans == 1e18:
  print(-1)
else:
  print(ans)