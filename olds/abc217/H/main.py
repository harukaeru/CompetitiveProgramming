#!/usr/bin/env python3
import sys


def solve(N: int, T: "List[int]", D: "List[int]", X: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        T[i] = int(next(tokens))
        D[i] = int(next(tokens))
        X[i] = int(next(tokens))
    solve(N, T, D, X)

if __name__ == '__main__':
    main()