#!/usr/bin/env python3
S = input()

current = '0'
s_cnt = 0
for i in range(len(S)):
  new_current = '1' if current == '0' else '0'
  if S[i] == current:
    s_cnt += 1
  current = new_current

current = '1'
t_cnt = 0
for i in range(len(S)):
  new_current = '1' if current == '0' else '0'
  if S[i] == current:
    t_cnt += 1
  current = new_current


print(min(s_cnt, t_cnt))