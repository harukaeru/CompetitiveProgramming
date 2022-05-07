#!/usr/bin/env python3
S = input()

MOD = 10 ** 9 + 7
word = 'chokudai'
dp = [0 for __ in range(len(word) + 1)]
dp[0] = 1

for s in S:
    for j, letter in enumerate(word):
        if letter == s:
            dp[j + 1] += dp[j] % MOD
            break
    # print(s, dp)
print(dp[len(word)] % MOD)
