N = 2 * 10 ** 3
M = 2 * 10 ** 3
P = M//2
print(N, M)
for i in range(M // 4):
    print(i + 1, (P + i + 1) % N + 1)
    print(i + 2, (P + i + 1) % N + 1)
    print(i + 3, (P + i + 1) % N + 1)
    print(i + 4, (P + i + 1) % N + 1)
    print(i + 5, (P + i + 1) % N + 1)
    print(i + 6, (P + i + 1) % N + 1)
    print(i + 7, (P + i + 1) % N + 1)
    print(i + 8, (P + i + 1) % N + 1)
    print(i + 9, (P + i + 1) % N + 1)
    print(i + 10, (P + i + 1) % N + 1)
