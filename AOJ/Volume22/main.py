def f(z, n, a):
    s = 0
    while n >= 0:
        s += a[n] % P * (z ** n) % P
        n -= 1
    return s

while 1:
    N, P = map(int, input().split())
    if N == P and P == 0:
        exit()

    *a, = map(int, input().split())

    count = 0
    for z in range(0, P):
        if f(z, N, a) % P == 0:
            count += 1
    print(count)
