#!/usr/bin/env python3.8
import sys


def solve(D: int, G: int, p: "List[int]", c: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    p = [int()] * (D)  # type: "List[int]"
    c = [int()] * (D)  # type: "List[int]"
    for i in range(D):
        p[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(D, G, p, c)

if __name__ == '__main__':
    main()
