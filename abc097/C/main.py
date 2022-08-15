#!/usr/bin/env python3
s = input()
k = int(input())

ans = set()
for l in range(1, 6):
  for i in range(len(s) - l + 1):
    c = s[i:i+l]
    ans.add(c)

ans = sorted(ans)
print(ans[k - 1])