#!/usr/bin/env python3.8
h1, h2, h3, w1, w2, w3 = map(int, input().split())

cnt = 0
for x0_0 in range(1, 29):
  for x0_1 in range(1, 29):
    for x1_0 in range(1, 29):
      for x1_1 in range(1, 29):
        x0_2 = h1 - x0_0 - x0_1
        x1_2 = h2 - x1_0 - x1_1
        x2_0 = w1 - x0_0 - x1_0
        x2_1 = w2 - x0_1 - x1_1
        if x0_2 > 0 and x1_2 > 0 and x2_0 > 0 and x2_1 > 0:
          x2_2_alpha = w3 - x0_2 - x1_2 
          x2_2_beta = h3 - x2_0 - x2_1
          if x2_2_alpha > 0 and x2_2_alpha == x2_2_beta:
            cnt += 1
print(cnt)