#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def resoudre(people, Q):
    """
    Renvoie un couple d'entier qui est la solution
    """
    grille = [[0 for i in xrange(Q)] for j in xrange(Q)]
    
    for p in people:
        (x, y, d) = p
        if d == 'N':
            for i in xrange(y+1, Q):
                for x in xrange(Q):
                    grille[x][i] += 1
            continue
        if d == 'S':
            for i in xrange(0, y):
                for x in xrange(Q):
                    grille[x][i] += 1
            continue
        if d == 'E':
            for i in xrange(x+1, Q):
                for y in xrange(Q):
                    grille[i][y] += 1
            continue
        if d == 'W':
            for i in xrange(0, x):
                for y in xrange(Q):
                    grille[i][y] += 1
            continue
    
    X, Y, m = 0, 0, 0
    for x in xrange(Q):
        for y in xrange(Q):
            if grille[x][y] > m:
                m = grille[x][y]
                X, Y = x, y
    return X, Y


def main():
    T = int(raw_input())
    for t in xrange(T):
        (P, Q) = map(int, raw_input().split(' '))
        people = []
        for p in xrange(P):
            line = raw_input().strip().split(' ')
            people.append( (int(line[0]), int(line[1]), line[2]) )
        resultat = resoudre(people, Q)
        print "Case #%d: %d %d" % (t+1, resultat[0], resultat[1])


if __name__ == '__main__':
    main()
