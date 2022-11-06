#!/usr/bin/env python3.8
import itertools

N, M = map(int, input().split())

paths = []
for i in range(M):
    a_i, b_i = map(int, input().split())
    # 調査不要
    if a_i == b_i:
        continue
    paths.append((a_i, b_i,))


paths_permutationed = list(itertools.permutations(paths))

from pprint import pprint
# pprint(paths_permutationed)

comb = 0
for paths in paths_permutationed:
    already_visited_cities = set([1])
    next_city = 1
    # if (paths[0] == (1, 3) or paths[0] == (3, 1)) and paths[1] == (3, 4) and paths[2] == (4, 5) and paths[3] == (5, 6) and paths[4] == (6, 7):
    #     should_print = True
    # else:
    #     should_print = False
    # if should_print:
    #     print(paths)
    for path in paths:
#         if should_print:
#             print('-- path', path)
        if not next_city in path:
            break
        copied_path = list(path[:])
        copied_path.remove(next_city)
#         if should_print:
#             print('copied', copied_path)

        next_city = copied_path[0]
        if next_city in already_visited_cities:
            break
        already_visited_cities.add(next_city)
        # if should_print:
        #     print('next_city', next_city)
        #     print('already', already_visited_cities)
        #     print('N', N)
        if len(already_visited_cities) == N:
            comb += 1
            break

print(comb)
