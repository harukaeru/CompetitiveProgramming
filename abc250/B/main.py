#!/usr/bin/env python3.8
N, A, B = map(int, input().split())

result = []
for j in range(A * N):
  row = []
  if j // A % 2 == 0:
    for i in range(B * N):
      if i // B % 2 == 0:
        row.append('.')
      else:
        row.append('#')
  else:
    for i in range(B * N):
      if i // B % 2 == 0:
        row.append('#')
      else:
        row.append('.')
  result.append(row)

for row in result:
  print(''.join(row))