import math

x1, y1, x2, y2 = map(float, input().split())

print(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
print(abs(complex(x2-x1, y2-y1)))
