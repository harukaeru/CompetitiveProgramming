child_dp = [0] * 241
adult_dp = [0] * 241
adult_dp[0] = 1

for i in range(241):
  if i + 5 <= 240:
    # こどもをうむ
    child_dp[i + 5] += adult_dp[i] * 10
    # 大人になったこどもと、こどもをうみ終わった大人を追加
    adult_dp[i + 5] += child_dp[i] + adult_dp[i]

print(child_dp)
print(adult_dp)

print('ans->', adult_dp[240])