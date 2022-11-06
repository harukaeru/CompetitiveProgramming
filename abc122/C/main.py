#!/usr/bin/env python3.8
N, Q = map(int, input().split())
S = input()

lr_list = []
for i in range(Q):
  l_i, r_i = map(int, input().split())
  lr_list.append((l_i, r_i))

marker = [0] * len(S)
for i in range(len(S) - 1):
  if S[i] == 'A' and S[i + 1] == 'C':
    marker[i + 1] = 1

marker_sum = [0] * len(S)
for i in range(len(S)):
  if i - 1 >= 0:
    marker_sum[i] = marker_sum[i - 1] + marker[i]
  else:
    marker_sum[i] = marker[i]
# print(marker)
# print(marker_sum)

for l_i, r_i in lr_list:
  ll = marker_sum[l_i - 1]
  rr = marker_sum[r_i - 1]
  # print('Si', ll, rr)
  print(rr - ll)