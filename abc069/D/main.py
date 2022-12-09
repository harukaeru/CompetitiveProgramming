#!/usr/bin/env python3.8
H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))

def generate():
  for i, a in enumerate(A, 1):
    for j in range(a):
      yield i

generator = generate()

ans = []
for i in range(H):
  x = [None] * W
  ans.append(x)

for i in range(H):
  if i % 2 == 0:
    for j in range(W):
      ans[i][j] = next(generator)
  else:
    for j in range(W - 1, -1, -1):
      ans[i][j] = next(generator)

for a in ans:
  print(*a)