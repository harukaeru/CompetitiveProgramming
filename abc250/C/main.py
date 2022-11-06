#!/usr/bin/env python3.8
N, Q = map(int, input().split())

num_to_pos = list(range(N))
pos_to_num = list(range(N))
for i in range(Q):
  x = int(input())
  pos = num_to_pos[x - 1]
  if pos == N - 1:
    pos -= 1
  
  num = pos_to_num[pos + 1]
  pos_to_num[pos], pos_to_num[pos + 1] = pos_to_num[pos + 1], pos_to_num[pos]
  num_to_pos[x - 1], num_to_pos[num] = num_to_pos[num], num_to_pos[x - 1]

print(' '.join(map(str, [n + 1 for n in pos_to_num])))