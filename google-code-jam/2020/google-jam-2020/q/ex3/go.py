#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys


def resoudre(taches):
    taches.sort()

    C, J = 0, 0
    solution = [' '] * len(taches)
    for tache in taches:
        (maintenant, fin, i) = tache

        if C <= maintenant:
            solution[i] = 'C'
            C = fin
            continue

        if J <= maintenant:
            solution[i] = 'J'
            J = fin
            continue

        return 'IMPOSSIBLE'

    return ''.join(solution)


def main():
    T = int(sys.stdin.readline())
    for t in xrange(1, T+1):
        N = int(sys.stdin.readline())
        taches = []
        for i in range(N):
            (debut, fin) = [int(s) for s in sys.stdin.readline().split(' ')]
            taches.append((debut, fin, i))
        solution = resoudre(taches)
        print "Case #%d: %s" % (t, solution)


if __name__ == '__main__':
    main()
