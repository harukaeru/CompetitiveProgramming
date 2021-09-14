H, W, C = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

INF = float('inf')
ans = INF

for _ in range(2):
    d = [[INF]*W for _ in range(H)]
    for i in range(H):
        anses = []
        for j in range(W):
            # 配列外参照を防ぐ
            if i:
                d[i][j] = min(d[i][j], d[i - 1][j])
            if j:
                d[i][j] = min(d[i][j], d[i][j - 1])
            print(A[i][j] + (i+j)*C + d[i][j], end=' ')
            ans = min(ans, A[i][j] + (i+j)*C + d[i][j])
            d[i][j] = min(d[i][j], A[i][j] - (i+j)*C)
        print()
    print('---------------')
    for v in A:
        v.reverse()

print(ans)
