#!/usr/bin/env python3.8
N, K = map(int, input().split())
A = list(map(int, input().split()))


def calc_apple_count(m):
  if m == 0:
    return 0, A[:]
  B = []
  cnt = 0
  for i in range(N):
    if A[i] >= m:
      B.append(A[i] - m)
      cnt += m
    else:
      B.append(0)
      cnt += A[i]
  return cnt, B

l = 0
r = 10 ** 12 + 1

while r - l > 1:
  mid = (r + l) // 2

  cnt, B = calc_apple_count(mid)
  # print(mid, ':', cnt)
  # print((l, r), cnt)
  if K < cnt:
    r = mid
  else:
    l = mid

cnt, B = calc_apple_count(l)
rest = K - cnt
i = 0
while rest > 0:
  if B[i] > 0:
    B[i] -= 1
    rest -= 1
  i += 1

print(*B)