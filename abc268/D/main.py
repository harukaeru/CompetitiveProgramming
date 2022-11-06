#!/usr/bin/env python3.8
from itertools import permutations

N, M = map(int, input().split())
S = []
for i in range(N):
  S.append(input())

string_count = sum([len(s) for s in S])
room = max(16 - (string_count + len(S) - 1), 0)
# print('string_count', string_count)
# print('room', room)

T = set()
for i in range(M):
  T.add(input())


interval = len(S) - 1
combs = []
# print('room', room)
for i in range((room + 1) ** interval):
  # print('---------------', i)
  data = []
  k = i
  for j in range(interval):
      data.append('_' * (k % (room + 1)))
      k //= (room + 1)

  # print(data)
  combs.append(data)

# from pprint import pprint# pprint(combs)

perm = permutations(S)
for x in perm:
  for comb in combs:
    s = ''
    if interval == 0:
      s = x[0]
    for k in range(interval):
      s += x[k] + '_' + comb[k]
    if interval > 0:
      s += x[k + 1]

    if s in T:
      continue

    if len(s) < 3 or len(s) > 16:
      continue
    print(s)
    exit()

print(-1)