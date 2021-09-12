A = [1, 2, 9, 10, 14, 15, 18, 19, 30, 32, 39, 40, 48, 50]

def is_ok(idx, key):
    return A[idx] >= key

def binary_search(a, key):
    left = -1
    right = len(a)

    while right - left > 1:
        mid = left + (right - left) // 2

        if is_ok(mid, key):
            right = mid
        else:
            left = mid
    return right

idx = binary_search(A, 13)
print(idx, A[idx])

idx = binary_search(A, 42)
print(idx, A[idx])

