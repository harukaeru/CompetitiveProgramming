#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(r: "List[int]", c: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    r = [int()] * (2)  # type: "List[int]"
    c = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(r, c)

if __name__ == '__main__':
    main()
