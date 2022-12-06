popcount=[0]*32
for i in range(1,32):
  popcount[i]=popcount[i//2]+(i%2)

def hypot(p,q):
  return ((p[0]-q[0])**2+(p[1]-q[1])**2)**0.5

N,M=map(int,input().split())
pos=[tuple(map(int,input().split())) for _ in range(N+M)]

dp=[[1e18]*(1<<(N+M)) for _ in range(N+M)]
for i in range(N+M): dp[i][1<<i]=hypot(pos[i],(0,0))

for s in range(1,1<<(N+M)):
  coef=0.5**popcount[s>>N]
  for i in range(N+M):
    if not (s>>i)&1: continue
    for j in range(N+M):
      if (s>>j)&1: continue
      new_dist=dp[i][s]+hypot(pos[i],pos[j])*coef
      if dp[j][s^(1<<j)]>new_dist: dp[j][s^(1<<j)]=new_dist

ans=1e18
for i in range(N+M):
  for s in range((1<<N)-1,1<<(N+M),1<<N):
    ans=min(ans,dp[i][s]+hypot(pos[i],(0,0))*0.5**popcount[s>>N])

print(f"{ans:.10f}")
