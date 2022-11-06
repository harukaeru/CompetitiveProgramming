#!/usr/bin/env python3.8
import sys
sys.setrecursionlimit(300000)

N = int(input())
G = {}
for i in range(N):
    G[i] = []

for __ in range(N - 1):
    A_i, B_i = map(int, input().split())
    A_i, B_i = A_i - 1, B_i - 1
    G[A_i].append(B_i)
    G[B_i].append(A_i)
for i in range(N):
    G[i] = list(sorted(G[i]))

first_arrived = {}
seen_dp = {}

ans = []
# @profile
def dfs(G, pos, pre):
    ans.append(pos)
    for nxt in G[pos]:
        if nxt != pre:
            dfs(G, nxt, pos)
            ans.append(pos)

def main():
    dfs(G, 0, -1)
    print(*[a+1 for a in ans])

main()
