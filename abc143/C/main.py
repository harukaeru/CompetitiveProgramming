#!/usr/bin/env python3.8
N = int(input())
S = input()

results = [S[0]]
current_candidate = S[0]
for i in range(1, N):
  if current_candidate != S[i]:
    current_candidate = S[i]
    results.append(S[i])

# print(results)
print(len(results))