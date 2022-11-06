#!/usr/bin/env python3.8
N = int(input())
A = list(map(int, input().split()))

lower_left = [0] * N
st_left = [(0, -1)]
for i in range(N):
  while st_left[-1][0] >= A[i]:
    st_left.pop()

  lower_left[i] = st_left[-1][1]
  st_left.append((A[i], i))

lower_right = [0] * N
st_right = [(0, N)]
for j in range(N):
  i = N - 1 - j
  while st_right[-1][0] >= A[i]:
    st_right.pop()

  lower_right[i] = st_right[-1][1]
  st_right.append((A[i], i))

max_s = 0
for i in range(N):
  le = lower_right[i] - lower_left[i] - 1
  s = A[i] * le
  max_s = max(max_s, s)


print(max_s)