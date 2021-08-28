import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

res1 = 0
res2 = 0
res3 = 0
res_inf = 0

for i in range(n):
    d = abs(y[i] - x[i])
    res1 += d
    d2 = d * d
    res2 += d2
    d3 = d2 * d
    res3 += d3
    res_inf = max(res_inf, d)

print(res1)
print(res2 ** (1/2))
print(res3 ** (1/3))
print(res_inf)
