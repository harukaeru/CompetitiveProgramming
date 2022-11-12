#!/usr/bin/env python3.8
N, D = map(int, input().split())
LR = []
for i in range(N):
  l, r = map(int, input().split())
  LR.append((l, r))
 
LR.sort(key=lambda x: (x[1], x[0]), reverse=True)
 
# print(LR)
l, r = LR.pop()
sep_l = r
sep_r = r + D - 1
cnt = 1

while len(LR) > 0:
  l, r = LR.pop()

  # print('sep', cnt, (l, r), [sep_l, sep_r], l<=sep_r)
  if l <= sep_r:
    continue
  sep_l = r
  sep_r = r + D - 1
  cnt += 1

print(cnt)