#!/usr/bin/env python3
N = int(input())

S = []
intermediate = False
for i in range(N):
    a = list(input())
    seta = set(a)
    if not intermediate and len(seta) == 1 and '.' in seta:
        continue
    intermediate = True
    S.append(a)

SS = []
intermediate = False
for i in range(len(S) - 1, -1, -1):
    s = S[i]
    seta = set(s)
    if not intermediate and len(seta) == 1 and '.' in seta:
        continue
    intermediate = True
    SS.append(s)
S = list(reversed(SS))

T = []
intermediate = False
for i in range(N):
    a = list(input())
    seta = set(a)
    if not intermediate and len(seta) == 1 and '.' in seta:
        continue
    intermediate = True
    T.append(a)

TT = []
intermediate = False
for i in range(len(T) - 1, -1, -1):
    t = T[i]
    seta = set(t)
    if not intermediate and len(seta) == 1 and '.' in seta:
        continue
    intermediate = True
    TT.append(t)
T = list(reversed(TT))

# p(S)
# print('------------')
# p(T)


def cut(A):
    row_length = len(A[0])
    sames = [set() for __ in range(row_length)]
    for s in A:
        for j in range(len(s)):
            sames[j].add(s[j])

    cutting_indexes = []
    # print('sames', sames)
    for i, s in enumerate(sames):
        if len(s) == 1 and '.' in s:
            cutting_indexes.append(i)
            continue
        break
    sames.reverse()
    # print('sames', sames)
    for i, s in enumerate(sames):
        if len(s) == 1 and '.' in s:
            cutting_indexes.append(row_length - 1 - i)
            continue
        break

    NEWS = []
    for s in A:
        row = []
        for j, v in enumerate(s):
            if j not in cutting_indexes:
                row.append(s[j])
        NEWS.append(row)
    return NEWS


def turn(A):
    A = list(reversed(A))
    row_length = len(A[0])

    new_a = []
    for j in range(row_length):
        r = []
        for i in range(len(A)):
            r.append(A[i][j])
        new_a.append(r)
    return new_a

def p(A):
    for a in A:
        print(a)

def is_same(A, B):
    h = len(A)
    w = len(A[0])
    for i in range(h):
        for j in range(w):
            try:
                if A[i][j] != B[i][j]:
                    return False
            except:
                return False
    h = len(B)
    w = len(B[0])
    for i in range(h):
        for j in range(w):
            try:
                if A[i][j] != B[i][j]:
                    return False
            except:
                return False
    return True

# p(S)
# print('-----------')
# print('t')
# p(T)
#
S = cut(S)
T = cut(T)
# print('cut--------')
# p(S)
# print('-----------')
# print('t')
# p(T)


if is_same(T, S):
    print('Yes')
    exit()

S = turn(S)
# print('------turn S')
# p(S)
if is_same(T, S):
    print('Yes')
    exit()

S = turn(S)
# print('------turn S')
# p(S)
if is_same(T, S):
    print('Yes')
    exit()

S = turn(S)
# print('------turn S')
# p(S)
if is_same(T, S):
    print('Yes')
    exit()

print('No')
