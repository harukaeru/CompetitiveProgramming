N = 2 * 10 ** 5
print(N)
for i in range(N):
    print(10 ** 9, end=' ')
    print(100, end=' ')
    if i > 101:
        for j in range(100):
            print(i - j - 1, end=' ')
    print()
