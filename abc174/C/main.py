#!/usr/bin/env python3
K = int(input())

r = {
    0: 7,
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1,
    7: 0,
    8: 9,
    9: 8,
}

first_k = K % 10
cache = {}
# 1桁目の数に何をかけると求める数が得られるかの表を生成する
# 2だったら、0は5をかけると手に入る、2は6をかけると手に入るという理屈
for i in range(10):
    for j in range(10):
        if (first_k * j) % 10 == i:
            cache[i] = j

current = 0
i = 1
while 1:
    print('current', current)
    # 今の1桁目をチェック
    d1 = current % 10  # 0

    # 1桁目と足し算して7になる数を取得する
    need = r[d1]  # 7

    # 足し算するための数を取得するために何をかけなければいけないかを取得する
    req = cache.get(need)

    # ↑そんなものが存在しなければ終了
    if req is None:
        print(-1)
        break

    # 次の桁を調べる
    current = (req * K + current) // 10
    if not current:
        print(i)
        break
    i += 1
