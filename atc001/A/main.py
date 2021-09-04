#!/usr/bin/env python3
H, W = map(int, input().split())
HW = []
pos = None

for i in range(H):
    w = list(input())
    if 's' in w:
        pos_w = w.index('s')
        pos = (i, pos_w)
    HW.append(w)

def DFS(HW, s_pos):

    seens = {}
    stacks = [s_pos]
    while len(stacks) > 0:
        current_pos = stacks.pop()
        for d in (1, 0), (0, 1), (-1, 0), (0, -1):
            try:
                new_pos = (current_pos[0] + d[0], current_pos[1] + d[1])
                if new_pos[0] < 0 or new_pos[1] < 0:
                    continue
                if seens.get(new_pos):
                    continue
                adj = HW[new_pos[0]][new_pos[1]]
                if adj == '#':
                    seens[new_pos] = True
                    continue
                elif adj == 'g':
                    print('Yes')
                    return
                elif adj == '.':
                    stacks.append(new_pos)

                seens[new_pos] = True
            except:
                pass
    print('No')

DFS(HW, pos)
