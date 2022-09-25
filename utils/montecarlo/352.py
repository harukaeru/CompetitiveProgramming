import random
N = 1000000

cnt = 0
for i in range(N):
  x = 6 * random.random()
  y = 9 * random.random()

  a = (x - 3) * (x - 3) + (y - 7) * (y - 7) <= 4
  b = (x - 3) * (x - 3) + (y - 3) * (y - 3) <= 9
  if a or b:
    cnt += 1

print(cnt / N)
print(54 * cnt / N)