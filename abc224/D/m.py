import random
N = 36
print(N)
for i in range(N):
    print(random.randint(1, 9), random.randint(1, 9))
x = list(range(1, 10))
random.shuffle(x)
print(*x[:8])
