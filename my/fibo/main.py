N = 10000

ans = [0] * N

ans[0] = 1
ans[1] = 1

for i in range(2, N):
    ans[i] = ans[i - 2] + ans[i - 1]

print(ans[30])
