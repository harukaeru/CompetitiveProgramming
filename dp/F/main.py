#!/usr/bin/env python3
s = input()
t = input()

dp = [
    [0 for __ in range(len(t) + 1)]
    for __ in range(len(s) + 1)
]
dp[0][0] = 0

for i in range(0, len(s)):
    for j in range(0, len(t)):
        # if i == 2 and j == 3:
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

ans_len = dp[len(s)][len(t)]

i = len(s)
j = len(t)
ans = []
while ans_len > 0:
    # print(i, j)
    # print(s[i], t[j])
    # print('-' * 20)
    if s[i - 1] == t[j - 1]:
        # print('i', 'j', i, j)
        ans.append(s[i - 1])
        ans_len -= 1
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i - 1][j]:
        i -= 1
    else:
        j -= 1
ans = ''.join(list(reversed(ans)))
print(ans)
