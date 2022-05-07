N = int(input())
S = input()

ans = S.count('R') * S.count('G') * S.count('B')
print('ans', ans)
for i in range(N):
    for j in range(i + 1, N):
        if (j + j - i < N) and ({S[i], S[j], S[j + j - i]} == {'R', 'G', 'B'}):
            ans -= 1

print(ans)
