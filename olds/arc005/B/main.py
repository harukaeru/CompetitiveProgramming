#!/usr/bin/env python3.8
import sys


def solve(x: int, y: int, W: str, c: "List[str]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    W = next(tokens)  # type: str
    c = [next(tokens) for _ in range(9)]  # type: "List[str]"
    solve(x, y, W, c)

if __name__ == '__main__':
    main()
