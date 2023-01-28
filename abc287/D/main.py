#!/usr/bin/env pypy3
from collections import deque


S = list(input())
T = list(input())

def match(a, b):
  return a == '?' or b == '?' or a == b


L = [0] * (len(T) + 1)
for i in range(len(T)):
  if match(S[i], T[i]):
    L[i + 1] = L[i] + 1
  else:
    break

S.reverse()
T.reverse()
R = [0] * (len(T) + 1)
for i in range(len(T)):
  if match(S[i], T[i]):
    R[i + 1] = R[i] + 1
  else:
    break

R.reverse()
for i in range(len(T) + 1):
  if L[i] + R[i] == len(T):
    print('Yes')
  else:
    print('No')