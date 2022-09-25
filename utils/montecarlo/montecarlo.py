import random
N = 10000000
cnt = 0

for i in range(N):
  x = random.random()
  y = random.random()
  if (x * x + y * y <= 1):
    cnt += 1

print(4 * cnt / N)