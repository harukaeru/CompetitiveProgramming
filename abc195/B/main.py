#!/usr/bin/env python3
import sys


def solve(A: int, B: int, W: int):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(A, B, W)

if __name__ == '__main__':
    main()
