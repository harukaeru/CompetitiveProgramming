#!/usr/bin/env python3.8
S = input()

cnt = 0
for s in S:
  if s == 'v':
    cnt += 1
  else:
    cnt += 2
print(cnt)