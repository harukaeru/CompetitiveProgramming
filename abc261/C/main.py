#!/usr/bin/env python3
from collections import defaultdict
N = int(input())
S = []
for i in range(N):
  S.append(input())

counter = defaultdict(int)

for i in range(N):
  cnt = counter[S[i]]
  if cnt == 0:
    print(S[i])
  else:
    print(S[i] + '(' + str(cnt) + ')')
  counter[S[i]] += 1