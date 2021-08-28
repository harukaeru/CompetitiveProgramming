N, Y = map(int, input().split())

for a in range(N + 1):
    for b in range(N - a + 1):
        # for c in range(N-a-b):
            c1000 = Y - (10000 * a + 5000 * b) #  + 1000 * c == Y:
            c = c1000 / 1000
            if (c1000 % 1000 == 0) and c == (N - a - b):
                print(a, b, int(c))
                # print(a + b + c)
                # print(a * 10000 + b * 5000 + c * 1000)
                exit()

print(-1, -1, -1)
