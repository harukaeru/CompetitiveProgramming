a = 1
b = 1

N = 10000000

if N >= 1:
  print(1)

if N >= 2:
  print(1)

for i in range(2, N):
  a, b = b, a + b
  print(b)