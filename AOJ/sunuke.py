N = int(input())

S_list = int(x) for x in input().replace('\n', '').split()
T_list = int(x) for x in input().replace('\n', '').split()

users = [{}] * N

t = max(max(S_list), max(T_list))
for i in range(1, t):
    if j in T_list:
        users[j][S_list[j]] += 1

    if k in S_list:
        for ll, user in enumerate(users):
            if user:
                users[ll + 1] = ll
