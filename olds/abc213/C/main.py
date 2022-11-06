#!/usr/bin/env python3.8
H, W, N = map(int, input().split())

hs = []
ws = []
hgroup = set()
wgroup = set()
for i in range(N):
    A_i, B_i = map(int, input().split())
    hs.append(A_i)
    ws.append(B_i)

    hgroup.add(A_i)
    wgroup.add(B_i)

hgroup = sorted(hgroup)
wgroup = sorted(wgroup)

def map_to_0(gr):
    i = 0
    current = -1
    mapped = []
    for g in gr:
        if current != g:
            i += 1
        mapped.append(i)
    return mapped

hgroup_mapped = map_to_0(hgroup)
wgroup_mapped = map_to_0(wgroup)

hmap = dict(zip(hgroup, hgroup_mapped))
wmap = dict(zip(wgroup, wgroup_mapped))

def convert(hs, hmap):
    return [hmap[v] for v in hs]

hhss = convert(hs, hmap)
wwss = convert(ws, wmap)

for i in range(N):
    print(hhss[i], wwss[i])
