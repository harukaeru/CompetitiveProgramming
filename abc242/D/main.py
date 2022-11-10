#!/usr/bin/env python3.8
S = input()
def forward(s, k):
  return chr(ord('A') + ('ABC'.index(s) + k) % 3)

def f(t, k):
  if t == 0:
    return S[k]
  if k == 0:
    return forward(S[0], t)
  if k % 2 == 0:
    return forward(f(t - 1, k // 2), 1)
  else:
    return forward(f(t - 1, (k - 1) // 2), 2)


Q = int(input())
for i in range(Q):
  t, k = map(int, input().split())
  print(f(t, k - 1))
