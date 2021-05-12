#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys


def contientDoublon(liste):
    dejaVu = set()
    for element in liste:
        if element in dejaVu:
            return True
        dejaVu.add(element)
    return False


def getColonne(matrice, n):
    for row in matrice:
        yield row[n]


def resoudre(matrice):
    k, r, c = 0, 0, 0
    for i in range(len(matrice)):
        k += matrice[i][i]

        row = matrice[i]
        if contientDoublon(row):
            r += 1

        col = getColonne(matrice, i)
        if contientDoublon(col):
            c += 1

    return k, r, c


def main():
    T = int(sys.stdin.readline())
    for i in xrange(1, T+1):
        N = int(sys.stdin.readline())
        matrice = []
        for j in xrange(N):
            ligne = [int(n) for n in sys.stdin.readline().split(' ')]
            matrice.append(ligne)
        (k, r, c) = resoudre(matrice)
        print "Case #%d: %d %d %d" % (i, k, r, c)


if __name__ == '__main__':
    main()
