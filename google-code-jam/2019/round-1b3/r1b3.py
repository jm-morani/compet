#!/usr/bin/env python
# -*- encoding: utf-8 -*-

###############################################################
# Toutes mes félicitations, cher Alb4tor, ainsi qu'à Madame ! #
# Tu as tant à transmettre que trois ne seront pas de trop.   #
###############################################################


def resoudre(N, K, C, D):
    """
    Renvoie un entier qui est la solution
    """
    total = 0
    for l in xrange(0, N):
        max_c = C[l]
        max_d = D[l]
        for r in xrange(l, N):
            max_c = max(max_c, C[r])
            max_d = max(max_d, D[r])
            if abs(max_c - max_d) <= K:
                total += 1

    return total


def main():
    T = int(raw_input())
    for t in xrange(T):
        (N, K) = map(int, raw_input().split(' '))
        C = map(int, raw_input().split(' '))
        D = map(int, raw_input().split(' '))
        resultat = resoudre(N, K, C, D)
        print "Case #%d: %s" % (t+1, resultat)


if __name__ == '__main__':
    main()
