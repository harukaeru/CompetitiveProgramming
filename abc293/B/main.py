#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

not_calls = set(range(1, N + 1))
for i in range(N):
  if i + 1 in not_calls:
    a = A[i]
    if a in not_calls:
      not_calls.remove(a)

ans = list(sorted(not_calls))
print(len(ans))
print(*ans)