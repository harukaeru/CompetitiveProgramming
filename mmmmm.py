#!/usr/bin/env python3.8
N = int(input())
P = list(map(int, input().split()))

Q = P + P[::]
max_cnt = -1
for iter in range(N):
  cnt = 0
  dishes = []
  for i in range(N):
    dish = Q[iter + i]
    dishes.append(dish)

    if dish in [(i - 1) % N, i % N, (i + 1) % N]:
      cnt += 1
  max_cnt = max(max_cnt, cnt)
  print(dishes)
print(max_cnt)


