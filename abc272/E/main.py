#!/usr/bin/env pypy3
N, M = map(int, input().split())
A = list(map(int, input().split()))

memo=[set() for _ in range(N + 1)]
 
for i, a in enumerate(A, 1):
  cnt = max(0, -(a // i))
  while a + i * cnt <= N:
    memo[a + i * cnt].add(cnt)
    cnt+=1
 
for i in range(1, M + 1):
  ans = 0
  while i in memo[ans]:
    ans+=1
  print(ans)