#!/usr/bin/env pypy3
import math

A, B = map(int, input().split())
g = math.gcd(A, B)

nums = []
for i in range(1, int(math.sqrt(g)) + 1):
  if g % i == 0:
    nums.append(i)
    if i != g // i:
      nums.append(g // i)
# print(nums)
nums.sort()

M = 10 ** 12 + 1
def is_prime(M):
  maxA = int(math.sqrt(M))
  for i in range(2,maxA+1):
      if M % i == 0:
        return False
  return True

cnt = 0
# print(primes)
for j in range(len(nums)):
  if is_prime(nums[j]):
    # print(nums[j])
    cnt += 1

print(cnt)