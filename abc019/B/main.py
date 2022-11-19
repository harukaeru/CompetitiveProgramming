#!/usr/bin/env python3.8
s = input()

cur = None
cnt = 0
ans = ''
for i, x in enumerate(s):
  if cur == x:
    cnt += 1

  if cur is None:
    cur = x
    cnt = 1
  elif cur != x:
    ans += cur
    ans += str(cnt)
    cur = x
    cnt = 1

  if i == len(s) - 1:
    ans += cur
    ans += str(cnt)
  
print(ans)