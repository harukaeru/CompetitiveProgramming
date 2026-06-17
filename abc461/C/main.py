#!/usr/bin/env python3.8
N, K, M = list(map(int, input().split()))

values = []
for i in range(N):
  c, v = list(map(int, input().split()))
  values.append((v, c))


values.sort()
values.reverse()
chosen = set()
m = 0
k = 0
ans = 0
chosen_value = set()
for i in range(N):
  v, c = values[i]
  if c not in chosen:
    m += 1
    k += 1
    ans += v
    chosen_value.add(i)
    chosen.add(c)
  if m == M:
    break

for i in range(N):
  if k == K:
    break
  if i in chosen_value:
    continue

  v, c = values[i]
  k += 1
  ans += v

print(ans)