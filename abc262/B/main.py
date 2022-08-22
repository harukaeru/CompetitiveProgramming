#!/usr/bin/env python3
n, m = map(int, input().split())

nodes = {}

for i in range(m):
  u, v = map(int, input().split())

  nodes.setdefault(u, set()).add(v)
  nodes.setdefault(v, set()).add(u)

# print(nodes)

cnt = 0
for a in range(1, 99):
  for b in range(a + 1, 100):
    for c in range(b + 1, 101):
      if nodes.get(a) and nodes.get(b) and nodes.get(c):
        if b in nodes[a] and c in nodes[b] and a in nodes[c]:
          cnt += 1

print(cnt)