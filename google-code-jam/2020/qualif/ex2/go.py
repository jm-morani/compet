#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys


def resoudre(S):
    solution = ''
    profondeur = 0
    for s in S:
        i = int(s)
        while i > profondeur:
            solution += '('
            profondeur += 1
        while i < profondeur:
            solution += ')'
            profondeur -= 1
        solution += s

    i = 0
    while i < profondeur:
        profondeur -= 1
        solution += ')'

    return solution


def main():
    N = int(sys.stdin.readline())
    for i in xrange(1, N+1):
        S = sys.stdin.readline().strip()
        solution = resoudre(S)
        print "Case #%d: %s" % (i, solution)


if __name__ == '__main__':
    main()
