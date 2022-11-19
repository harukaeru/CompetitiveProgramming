#!/usr/bin/env python3.8
n = int(input())
A = list(map(int, input().split()))

# i % 3 == 2
# i % 2 == 0
def f(a):
  cnt = 0
  while a % 3 == 2 or a % 2 == 0:
    cnt += 1
    a -= 1
  return cnt
  

tot = 0
for a in A:
  # print(f(a))
  tot += f(a)
print(tot)