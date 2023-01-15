#!/usr/bin/env python3.8
N = int(input())

poses = []
mx = 0
my = 0
for i in range(N):
  a,b,c,d=map(int, input().split())
  poses.append((a,b,c,d))
  mx = max(mx, max(a, c))
  my = max(my, max(b, d))

papers = []
for i in range(my + 2):
  papers.append([0] * (mx + 2))

for i in range(N):
  a,b,c,d = poses[i]
  c -= 1
  d -= 1
  papers[b][a] += 1
  papers[b][c + 1] -= 1
  papers[d + 1][a] -= 1
  papers[d + 1][c + 1] += 1

for i in range(1, my + 2):
  for j in range(mx + 2):
    papers[i][j] += papers[i - 1][j]

for i in range(my + 2):
  for j in range(1, mx + 2):
    papers[i][j] += papers[i][j - 1]

cnt = 0
for p in papers:
  cnt += len([x for x in p if x > 0])
print(cnt)
