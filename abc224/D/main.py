#!/usr/bin/env pypy3
from collections import defaultdict, deque


G = defaultdict(list)
M = int(input())
for i in range(M):
  u,v = map(int, input().split())
  G[u].append(v)
  G[v].append(u)

p = tuple(map(int, input().split()))

emp = set(range(1, 10)) - set(p)
ans = tuple(range(1, 9))
e = emp.pop()

K = 36

q = deque()
q.append((p, e, 0))

seen = set()
seen.add(p)
while len(q) > 0:
  p, e, cnt = q.popleft()
  if p == ans:
    print(cnt)
    exit()

  for pos in G[e]:
    try:
      i = p.index(pos)
    except:
      continue
    t = tuple(p[:i] + (e,) + p[i + 1:])
    # print(cnt, '  ' * cnt, 't', t)
    if t not in seen:
      seen.add(t)
      q.append((t, pos, cnt + 1))

print(-1)
