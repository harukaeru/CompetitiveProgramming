#!/usr/bin/env python3.8
S = input()

groups = S.split('+')
cnt = 0
for g in groups:
  if '0' not in g:
    cnt += 1
print(cnt)