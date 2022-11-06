#!/usr/bin/env python3.8
N, K = map(int, input().split())

t = K // N
n = K % N

kosuu = [t] * N

*a, = map(int, input().split())
m = dict(zip(a, list(range(N))))

nums = []
for id in sorted(a):
    nums.append(m[id])

# print('nums', nums)
i = 0
while n > 0:
    kosuu[nums[i]] += 1
    i += 1
    n -= 1

for i in range(N):
    print(kosuu[i])
