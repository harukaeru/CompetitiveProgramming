import random

def r(n):
    return random.randint(1, n)

N = r(10)
M = N - 2 + r(8)
print(f"{N} {M}")

ns = list(range(1, N + 1))
for i in range(1, M + 1):
    if len(ns) > 0:
        x = ns.pop()
    else:
        x = r(N)

    print(x, r(N), r(10) - 5)
