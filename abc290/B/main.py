#!/usr/bin/env python3.8
N,K=map(int, input().split())
S = input()


ans = ''
for i in range(N):
  if S[i] == 'o' and K >= 1:
    K -= 1
    ans += 'o'
  else:
    ans += 'x'
print(ans)