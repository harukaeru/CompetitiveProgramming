def f(x):
  return 2 ** (x * x)

s = 0
p = 0
while p < 1:
  s += f(p) * 0.00001
  p += 0.00001

print(s)