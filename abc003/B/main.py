#!/usr/bin/env python3.8
S = input()
T = input()

symbols = 'atcoder'
for i in range(len(S)):
  if S[i] == T[i]:
    continue
  if S[i] == '@' and T[i] in symbols:
    continue
  if T[i] == '@' and S[i] in symbols:
    continue

  print('You will lose')
  exit()
print('You can win')