#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(S: str, K: int):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    K = int(next(tokens))  # type: int
    solve(S, K)

if __name__ == '__main__':
    main()
