#!/usr/bin/env python3.8
sx,sy,tx,ty=map(int, input().split())

ans = ''

ans += 'U' * (ty - sy)
ans += 'R' * (tx - sx)
ans += 'D' * (ty - sy)
ans += 'L' * (tx - sx)

ans += 'L'
ans += 'U' * (ty - sy)
ans += 'UR'
ans += 'R' * (tx - sx)
ans += 'D'

ans += 'R'
ans += 'D' * (ty - sy)
ans += 'DL'
ans += 'L' * (tx - sx)
ans += 'U'

print(ans)
