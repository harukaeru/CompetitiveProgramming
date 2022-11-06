#!/usr/bin/env python3.8
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans1 = 0
for i in range(N):
  if A[i] == B[i]:
    ans1 += 1

b_dict = {}
for i, b in enumerate(B):
  b_dict[b] = i

ans2 = 0
for i in range(N):
  if A[i] in b_dict:
    j = b_dict[A[i]]
    if i != j:
        ans2 += 1

print(ans1)
print(ans2)