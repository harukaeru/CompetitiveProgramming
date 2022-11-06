#!/usr/bin/env python3.8
N = int(input())

points = []
point_set = set()
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))
    point_set.add((x, y))

count = 0
for i in range(N):
    p0 = points[i]
    for j in range(N):
        p1 = points[j]
        if (p0[0] < p1[0] and p0[1] < p1[1]):
            if (p0[0], p1[1]) in point_set and (p1[0], p0[1]) in point_set:
                count += 1

print(count)
