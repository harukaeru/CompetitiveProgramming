#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

row = []
for i, a in enumerate(A):
  j = i + 1
  a_n = a - j
  row.append(a_n)

row.sort()

m = None
if N % 2 == 1:
  m = row[N // 2]
else:
  m = (row[N // 2] + row[N // 2 - 1]) // 2

total = 0
for r in row:
  total += abs(r - m)

print(total)