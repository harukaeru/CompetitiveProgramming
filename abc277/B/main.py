#!/usr/bin/env python3.8
N = int(input())
S = []
for i in range(N):
  S.append(input())

X = set(['H', 'D', 'C', 'S'])
Y = set(['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K'])
ng = False
for s in S:
  if s[0] not in X:
    ng = True

  if s[1] not in Y:
    ng = True


if len(set(S)) != len(S):
  ng = True
if ng:
  print('No')
else:
  print('Yes')