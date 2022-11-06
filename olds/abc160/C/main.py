#!/usr/bin/env python3.8
K, N = map(int, input().split())
*A, = map(int, input().split())

distances = []
for i in range(len(A)):
    if i == len(A) - 1:
        distances.append(abs(K - A[i]) + A[0])
    else:
        distances.append(abs(A[i + 1] - A[i]))

# print('d', distances)
minimum = sum(distances) - max(distances)

print(minimum)
