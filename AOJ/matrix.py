n, m, l = map(int, input().split())

a = []
for __ in range(n):
    a.append(list(map(int, input().split())))

b = []
for __ in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for j in range(l):
        s = 0
        for k in range(m):
            s += a[i][k] * b[k][j]
        if j == l - 1:
            print(s)
        else:
            print(s, end=' ')
