#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from collections import defaultdict


def genPrefixe(rev):
    for l in range(1, len(rev)+1):
        yield rev[0:l]


def resoudre(mots):
    reversed = [mot[::-1] for mot in mots]

    prefixes = defaultdict(int)
    for rev in reversed:
        for prefixe in genPrefixe(rev):
            prefixes[prefixe] += 1

    total = 0
    m = len(mots)
    while True:
        sub = filter(lambda x: x[1] < 2, prefixes.iteritems())
        for prefixe, nb in sub:
            del prefixes[prefixe]
        
        # print total, prefixes
        if len(prefixes) == 0:
            break

        for n in range(2, m+1):
            for prefixe, nb in prefixes.iteritems():
                if nb == n:
                    # print "> %s" % prefixe
                    total += 2
                    del prefixes[prefixe]
                    for prefixe in genPrefixe(prefixe[:-1]):
                        prefixes[prefixe] -= 2
                    n = -1
                    break
            if n < 0:
                break

    return total


def test():
    pass


def main():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        mots = [raw_input().strip() for n in xrange(N)]
        print "Case #%d: %d" % (t+1, resoudre(mots))


if __name__ == '__main__':
    if 'test' in sys.argv:
        test()
    else:
        main()
