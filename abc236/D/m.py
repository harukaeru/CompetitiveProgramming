N = 6
print(N)
for i in range(2 * N + 1):
    ps = []
    j = i + 2
    while j <= 2 * N:
        ps.append(99999999)
        j += 1
    print(*ps)
