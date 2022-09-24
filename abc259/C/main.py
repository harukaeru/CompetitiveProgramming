#!/usr/bin/env python3
S = input()
T = input()

def runlength(s):
  cnt = 1
  data = []
  for i in range(1, len(s)):
    if s[i] != s[i - 1]:
      data.append((s[i - 1], cnt))
      cnt = 1
    else:
      cnt += 1
  data.append((s[i], cnt))
  return data

rs = runlength(S)
rt = runlength(T)

if len(rs) != len(rt):
  print('No')
  exit()

for i in range(len(rs)):
  if rs[i][0] != rt[i][0]:
    print('No')
    exit()

  if rs[i] == rt[i]:
    continue
  if rs[i][1] <= 1:
    print('No')
    exit()
  if rs[i][1] > rt[i][1]:
    print('No')
    exit()
print('Yes')