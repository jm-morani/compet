#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from itertools import chain




def debug(msg):
    """
    Debug avec script interactive_runner.py modifiée
    """
    sys.stderr.write(str(msg) + "\n")
    sys.stderr.flush()


def echo(chaine):
    sys.stdout.write(chaine + "\n")
    sys.stdout.flush()
    debug(" <- " + chaine)


def readline():
    rcv = sys.stdin.readline().strip()
    debug(" -> " + rcv)
    return rcv


#
def decompter(liste, ref):
    n = 0
    liste = list(liste) # TODO Utilser chain
    while len(liste) > 0:
        c = liste[0]
        if c == ref:
            liste.pop(0)
            n += 1
        else:
            return n
    return n


def Compteur(sequence, avec_valeur=False):
    """
    Generateur comptant les valeurs
    successives identiques
    """
    n = 0
    ref = sequence[0]
    for c in sequence:
        if c == ref:
            n += 1
        else:
            yield (n, ref) if avec_valeur else n
            n = 1
            ref = c
    yield (n, ref) if avec_valeur else n


class Resolveur():
    def __init__(self, N, B, F):
        self.i = -1
        self.N = N
        self.B = B
        self.F = F
        self.recu = [0] * (N - B)

    def proposer(self):
        self.i += 1
        if self.i+1 > self.F:
            manquant = set(xrange(self.N)) - set(self.recu)
            manquant = sorted(list(manquant))
            return " ".join([str(m) for m in manquant])

        proposition = [1 & (x >> self.i) for x in xrange(self.N)]

        return "".join([str(i) for i in proposition])

    def recevoir(self, reponse):
        self.recu = [x + (y << self.i) for x,y in zip(self.recu, reponse)]


def main():
    """
    Resolution interactive
    """
    T = int(sys.stdin.readline())
    for i in xrange(T):
        debug("== Test %d ==" % (i+1))
        N, B, F = [int(x) for x in readline().split(' ')]
        resolveur = Resolveur(N, B, F)

        for i in range(F+1):
            proposition = resolveur.proposer()
            echo(proposition)

            rcv = readline()
            if rcv == "-1":
                sys.exit(0)

            if " " in proposition:
                break

            resolveur.recevoir([int(c) for c in rcv])


if __name__ == '__main__':
    main()
