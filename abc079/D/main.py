#!/usr/bin/env python3
import sys


def solve(H: int, W: int, c: "List[List[int]]", A: "List[List[int]]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    c = [[int(next(tokens)) for _ in range(9 + 1)] for _ in range(9 + 1)]  # type: "List[List[int]]"
    A = [[int(next(tokens)) for _ in range(W)] for _ in range(H)]  # type: "List[List[int]]"
    solve(H, W, c, A)

if __name__ == '__main__':
    main()
