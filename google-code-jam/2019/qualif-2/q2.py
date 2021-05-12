#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys


def resoudre(N, path):
    return path.replace('E', 'X').replace('S', 'E'). replace('X', 'S')


def main():
    T = int(sys.stdin.readline())
    for i in xrange(1, T+1):
        N = int(sys.stdin.readline())
        path = sys.stdin.readline().strip()
        res = resoudre(N, path)
        print "Case #%d: %s" % (i, res)


if __name__ == '__main__':
    main()
