#!/usr/bin/env python3.8
N = int(input())
S = input()

min_d = 3 * (10 ** 5) + 1
w_counter = [0] * (N + 1)
for i in range(N):
  w_counter[i + 1] += w_counter[i]
  if S[i] == 'W':
    w_counter[i + 1] += 1

e_counter = [0] * (N + 1)
S2 = S[::-1]
for i in range(N):
  e_counter[i + 1] += e_counter[i]
  if S2[i] == 'E':
    e_counter[i + 1] += 1
e_counter.reverse()

# print(w_counter)
# print(e_counter)
for i in range(1, N + 1):
  # a = S[:i].count('W')
  a = w_counter[i - 1]
  # b = S[i + 1:].count('E')
  b = e_counter[i]
  min_d = min(min_d, a + b)
  
print(min_d)