import math

a, b, C = map(int, input().split())

r = C * math.pi / 180
S = a * b * math.sin(r) / 2
c_pow2 = a ** 2 + b ** 2 - 2 * a * b * math.cos(r)
c = math.sqrt(c_pow2)
L = a + b + c
h = b * math.sin(r)

print(S)
print(L)
print(h)
