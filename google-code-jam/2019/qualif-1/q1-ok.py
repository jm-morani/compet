#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

class NotSolvable(BaseException):
    pass


def resoudre(X, racine=True):
    if X <= 0:
        return (0, 0)

    x, r = divmod(X, 10)
    for c in xrange(10):
        retenu = 0
        a, b = (c, r - c)

        if b < 0:
            b = b + 10
            retenu += 1

        if (a == 4) or (b == 4):
            continue

        if a + b > 10:
            retenu += 1

        try:
            A, B = resoudre(x-retenu, False)
            A, B = 10*A+a, 10*B+b
            if racine and ((A == 0) or (B == 0)):
                continue
            return (A, B)
        except NotSolvable:
            continue
    raise NotSolvable()


def main():
    N = int(sys.stdin.readline())
    for i in xrange(1, N+1):
        x = int(sys.stdin.readline())
        (a, b) = resoudre(x)
        print "Case #%d: %d %d" % (i, a, b)


if __name__ == '__main__':
    main()
