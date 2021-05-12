#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

class Found(BaseException):
    def __init__(self, r, c, found=None):
        self.suivants = [(r, c)]
        if found:
            self.suivants.extend(found.suivants)


def DepartsPossibles(R, C):
    """
    Départs possibles limités à un huitième ou un quart
    équivalent à l'ensemble des cases par symmétrie.
    """
    demiR = R  / 2 + 1
    demiC = C  / 2 + 1
    if R == C:
        for r in range(demiR):
            for c in range(demiC):
                if c <= r:
                    yield (r, c)
    else:
        for r in range(demiR):
            for c in range(demiC):
                yield (r, c)


def deplacer(reste, _r, _c):
    for possible in list(reste):
        r, c = possible
        if (r == _r) or (c == _c):
            continue
        if (r + c == _r + _c) or (r - c == _r - _c):
            continue
        reste.remove(possible)

        if not reste:
            raise Found(r, c)

        try:
            deplacer(reste, r, c)
        except Found as e:
            raise Found(r, c, e)

        reste.add(possible)


def resoudre(R, C):
    """
    Renvoie None si impossible
    Renvoie une liste de tuple (x, y) sinon (indexé de 0 à c
    """
    reste = set([(r, c) for c in range(C) for r in range(R)])

    for depart in DepartsPossibles(R, C):
        r, c = depart

        try:
            deplacer(reste, r, c)
        except Found as e:
            return e.suivants  # POSSIBLE

    return []  # IMPOSSIBLE


def verif(R, C, resultat):
    if len(resultat) != R * C:
        return "ECHEC : Pas autant de visite que de case"

    grille = [[False] * C] * R
    (r, c) = resultat.pop(0)
    while True:
        if r < 0 or r >= R:
            return "ECHEC : r=%d" % r
        if c < 0 or c >= C:
            return "ECHEC : c=%d" % c
        if grille[r][c]:
            return "ECHEC : %d, %d déjà visité" % (r, c)
        if len(resultat) == 0:
            return "OK"
        _r, _c = r, c
        (r, c) = resultat.pop(0)
        if _r == r:
            return "ECHEC : r=r' (%d, %d)" % (r, _r)
        if _c == c:
            return "ECHEC : c=c' (%d, %d)" % (c, _c)
        if (r - c == _r - _c) or (r + c == _r + _c):
            return "ECHEC : diag (%d, %d) / (%d, %d)" % (r, c, _r, _c)


def test():
    lst = ((2, 2), (2, 5), (3, 3), (2,4), (2, 6), (4, 4), (5, 5), (4, 5), (7, 5))
    for (R, C) in lst:
        resultat = resoudre(R, C)
        if resultat:
            msg = verif(R, C, resultat)
            print "(%d, %d) => POSSIBLE => %s" % (R, C, msg)
            if msg != "OK":
                print repr(resultat)
        else:
            print "(%d, %d) => IMPOSSIBLE => ??" % (R, C)


def main():
    T = int(raw_input())
    for t in xrange(T):
        (R, C) = map(int, raw_input().split(' '))
        resultat = resoudre(R, C)
        if resultat:
            print "Case #%d: POSSIBLE" % (t+1)
            for (r, c) in resultat:
                print "%d %d" % (r+1, c+1)
        else:
            print "Case #%d: IMPOSSIBLE" % (t+1)


if __name__ == '__main__':
    if 'test' in sys.argv:
        test()
    else:
        main()
