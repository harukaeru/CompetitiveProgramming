#!/usr/bin/env python3.8
N = int(input())
X = list(map(int, input().split()))
Y = [y for y in X]

Y.sort()

left = Y[:N//2]
last_left = left[-1]
right = Y[N//2:]
first_right = right[0]

left = set(left)
right = set(right)

for x in X:
  if x in left:
    print(first_right)
  else:
    print(last_left)