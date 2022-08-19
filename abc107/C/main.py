#!/usr/bin/env python3
N, K = map(int, input().split())
x = list(map(int, input().split()))

minuses = [0]
pluses = [0]
for x_i in x:
  if x_i >= 0:
    pluses.append(x_i)
  else:
    minuses.append(-x_i)

pluses.sort()
minuses.sort()

ans = 999999999999
for i in range(len(pluses)):
  j = K - i
  if 0 <= j < len(minuses):
    ans = min(ans, pluses[i] * 2 + minuses[j])

for i in range(len(minuses)):
  j = K - i
  if 0 <= j < len(pluses):
    ans = min(ans, minuses[i] * 2 + pluses[j])

print(ans)
