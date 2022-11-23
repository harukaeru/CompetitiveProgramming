def is_ok(v):
    if A[v] >= 13:
        return True
    return False

def binary_search(a):
    left = -1
    right = len(a)

    while (right - left) > 1:
        mid = left + (right - left) // 2

        if is_ok(mid):
            right = mid
        else:
            left = mid
    return right



A = [1, 2, 9, 10, 14, 15, 18, 19, 30, 32, 39, 40, 48, 50]

idx = binary_search(A)
print('idx', idx, A[idx])
