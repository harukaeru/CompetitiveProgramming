#!/usr/bin/env python3.8
s = input()
k = int(input())

X = set()
for i in range(len(s) - k + 1):
  # print('i', i)
  X.add(s[i:i+k])
print(len(X))