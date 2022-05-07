import random
n = random.randint(1, 5)

def r(x):
    return random.randint(1, x + 1)

m = r(5)

print(n, m)
seed = r(100)
for i in range(1, n + 1):
    s = seed + 7 * (i - 1)
    for j in range(m):
        print(str(s + j), end=' ')
    print()
