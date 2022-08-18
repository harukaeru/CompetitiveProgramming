#!/usr/bin/env python3
D, G = map(int, input().split())
scores = []
for i in range(D):
  p, c = map(int, input().split())
  scores.append((p, c))


all_selected = sum([s[0] + 1 for s in scores])
dp = []

for d in range(D + 1):
  dp.append([0] * all_selected)

min_count = 99999999999
for i, (problem_count, complete) in enumerate(scores):

  for j in range(len(dp[i]) - problem_count):
    for count in range(problem_count + 1):
      obtained_score = (i + 1) * 100 * count
      if count == problem_count:
        obtained_score += complete

      dp[i + 1][j + count] = max(obtained_score + dp[i][j], dp[i][j + count], dp[i + 1][j+count])
      # print(dp[i + 1])
      if dp[i + 1][j + count] >= G:
        min_count = min(min_count, j + count)

print(min_count)

# ps = [s[0] + 1 for s in scores]
# 
# m = 1
# for p in ps:
#   m *= p

# ans = 999999999
# print('m', m)
# for i in range(m):
#   tmp = i
#   current_score = 0
#   total_count = 0
#   for score_i, p in enumerate(ps):
#     count = tmp % p
#     total_count += count
#     current_score += (score_i + 1) * 100 * count
#     if count == p - 1:
#       bonus = scores[score_i][1]
#       current_score += bonus
#     tmp //= p
# 
#   if current_score >= G:
#     ans = min(ans, total_count)