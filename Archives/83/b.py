N, A, B = map(int, input().split())

s = 0
for i in range(N + 1):
    ans = sum(int(j) for j in str(i))
    if A <= ans <= B:
        s += i

print(s)
