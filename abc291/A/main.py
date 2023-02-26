#!/usr/bin/env python3.8
S = input()
for i in range(len(S)):
  if S[i] == S[i].upper():
    print(i + 1)
    exit()