N=int(input())
T=list(map(int,input().split()))
M=10**5
INF=10**9
DP=[[INF]*(M+1001) for i in range(N+1)]
DP[0][0]=0
for i in range(N):
  for j in range(M+1):
    DP[i+1][j]=min(DP[i+1][j],DP[i][j]+T[i])
    DP[i+1][j+T[i]]=min(DP[i+1][j+T[i]],DP[i][j])
ANS=INF
for i in range(M+1):
  ANS=min(ANS,max(i,DP[N][i]))
print(ANS)
