#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import sys


VIDE = '.'
OCCUPE = 'O'
RADIOACTIF = '#'


class Boom(BaseException):
    pass


class Gagne(BaseException):
    pass


class Grille():
    def __init__(self, R, C, data):
        self.R = R
        self.C = C
        self.data = data

    def clone(self):
        return Grille(self.R, self.C, self.data)

    def getVides(self):
        vides = filter(
            lambda (r, c): self.get(r, c) == VIDE,
            [(r, c) for r in xrange(self.R) for c in xrange(self.C)]
        )
        return vides

    def get(self, r, c):
        return self.data[r * self.C + c]

    def put(self, r, c):
        i = r * self.C + c
        
        if r < 0 or r >= self.R:
            return False
        if c < 0 or c >= self.C:
            return False
        
        if self.data[i] == VIDE:
            self.data[i] = OCCUPE
            return True

        if self.data[i] == RADIOACTIF:
            raise Boom()

        return False

    def put_H(self, r, c):
        self.put(r, c)

        x = c - 1
        while self.put(r, x):
            x -= 1

        x = c + 1
        while self.put(r, x):
            x += 1

    def put_V(self, r, c):
        self.put(r, c)

        x = r - 1
        while self.put(x, c):
            x -= 1

        x = r + 1
        while self.put(x, c):
            x += 1

    def dump(self, t=0):
        for r in xrange(self.R):
            print "  " * t,
            for c in xrange(self.C):
                print self.get(r, c),
            print
        print


def jouer_Terry(grille, r, c, d, t=0):
    """
    r, c = row, col
    Direction V, H
    t = tour (%2 = 0 --> Becca)
    """
    print "%sTERRY r=%d, c=%d, d=%c" % ("  "*t, r, c, d)

    grille = grille.clone()
    R, C = grille.R, grille.C

    try:
        if d == 'H':
            grille.put_H(r, c)
        elif d == 'V':
            grille.put_V(r, c)
        grille.dump(t)
    except Boom:
        return

    # Tour de Becca
    vides = grille.getVides()
    if len(vides) == 0:
        return

    for (r, c) in vides:
        for d in ('H', 'V'):
            jouer_Becca(grille, r, c, d, t+1)


def jouer_Becca(grille, r, c, d, t=0):
    """
    r, c = row, col
    Direction V, H
    t = tour (%2 = 0 --> Becca)
    """
    print "%sBECCA r=%d, c=%d, d=%c" % ("  "*t, r, c, d)

    grille = grille.clone()
    R, C = grille.R, grille.C

    try:
        if d == 'H':
            grille.put_H(r, c)
        elif d == 'V':
            grille.put_V(r, c)
        grille.dump(t)
    except Boom:
        return

    # Tour de Terry
    vides = grille.getVides()
    print vides
    if len(vides) == 0:
        raise Gagne

    for (r, c) in vides:
        for d in ('H', 'V'):
            jouer_Terry(grille, r, c, d, t+1)


def resoudre(grille):
    """
    Renvoie un entier qui est la solution
    """
    nbOuvertures = 0

    vides = grille.getVides()
    for (r, c) in vides:
        for d in ('H', 'V'):
            try:
                jouer_Becca(grille, r, c, d)
            except Gagne:
                nbOuvertures += 1
            except Boom:
                pass
    return nbOuvertures


def main():
    T = int(raw_input())
    for t in xrange(T):
        (R, C) = map(int, raw_input().split(' '))
        data = ''.join([raw_input().strip() for r in xrange(R)])
        grille = Grille(R, C, list(data))
        resultat = resoudre(grille)
        print "Case #%d: %s" % (t+1, resultat)


def test():
    R = 4
    C = 5
    data = []
    data.append('.....')
    data.append('.....')
    data.append('.....')
    data.append('....#')
    grille = Grille(R, C, list(''.join(data)))
    print list(''.join(data))
    grille.dump()
    jouer(grille, 0, 3, 'V', 0)
    # jouer(grille, 2, 4, 'H')
    jouer(grille, 2, 1, 'H', 0)
    #resultat = resoudre(grille)
    #print "Case #%d: %s" % (t+1, resultat)


if __name__ == '__main__':
    if 'test' in sys.argv:
        test()
    else:
        main()
