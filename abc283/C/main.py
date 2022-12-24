#!/usr/bin/env python3.8
S = input()

cnt = 0
i = 0
while i < len(S):
  if S[i] != '0':
    cnt += 1
    i += 1
    continue

  if i + 1 < len(S) and S[i + 1] == '0':
    i += 2
    cnt += 1
    continue
  else:
    i += 1
    cnt += 1
  # print(i)
print(cnt)