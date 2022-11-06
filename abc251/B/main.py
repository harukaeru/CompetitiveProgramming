#!/usr/bin/env python3.8
N, W = map(int, input().split())
A = list(map(int, input().split()))

counter = [0] * (W + 1)

for i in range(len(A)):
  a = A[i]
  if a <= W:
    counter[a] += 1

  for j in range(i + 1, len(A)):
    b = A[j]
    if a + b <= W:
      counter[a + b] += 1
    for k in range(j + 1, len(A)):
      c = A[k]
      if a + b + c <= W:
        counter[a + b + c] += 1

cnt = 0
for c in counter:
  if c >= 1:
    cnt += 1

print(cnt)
