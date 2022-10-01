#!/usr/bin/env python3
S = input()

ms = [
  [7],
  [4],
  [2, 8],
  [1, 5],
  [3, 9],
  [6],
  [10],
]

columns = set()
for i, s in enumerate(S):
  j = i + 1
  if j == 1 and s == '1':
    print('No')
    exit()

  if s == '0':
    continue

  column = None
  for c, vs in enumerate(ms):
    if j in vs:
      column = c + 1
  columns.add(column)

if not columns:
  print('No')
  exit()

mi = min(columns)
ma = max(columns)
if ma - mi + 1 == len(columns):
  print('No')
else:
  print('Yes')