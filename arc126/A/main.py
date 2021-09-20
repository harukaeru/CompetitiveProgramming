#!/usr/bin/env python3
T = int(input())

def solve(n_2, n_3, n_4):
    m_1, m_3, m_2 = n_2, n_3 // 2, n_4
    # print('m_1, m_2, m_3', m_1, m_2, m_3)
    ans = 0
    if m_3 >= 1 and m_2 >= 1:
        count = min(m_3, m_2)
        m_2 = m_2 - count
        m_3 = m_3 - count
        ans += count

    if m_3 >= 1 and m_1 >= 2:
        count = min(m_3, m_1 // 2)
        m_3 = m_3 - count
        m_1 = m_1 - count * 2
        ans += count

    if m_2 >= 2 and m_1 >= 1:
        count = min(m_2 // 2, m_1)
        m_2 = m_2 - count * 2
        m_1 = m_1 - count
        ans += count

    if m_2 >= 1 and m_1 >= 3:
        count = min(m_2, m_1 // 3)
        m_2 = m_2 - count
        m_1 = m_1 - count * 3
        ans += count

    if m_1 >= 5:
        count = m_1 // 5
        m_1 = m_1 - count
        ans += count
    return ans


for i in range(T):
    n_2, n_3, n_4 = map(int, input().split())
    print(solve(n_2, n_3, n_4))
    # break
    # maximum = (n_2 * 2 + n_3 * 3 + n_4 * 4) // 10
    # left = -1
    # right = maximum + 1
    # while right - left > 1:
    #     mid = left + (right - left) // 2
    #     if is_match(mid):
    #         right = mid
    #     else:
    #         left = mid
    # print(right)

# 10 = 4 + 4 + 2
# 10 = 4 + 3 + 3
# 10 = 4 + 2 + 2 + 2
# 10 = 3 + 3 + 2 + 2
# 10 = 2 + 2 + 2 + 2 + 2
