#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from itertools import chain

OK = 'ok'
HS = 'hs'
INCONNU = '??'


class Resultat(BaseException):
    def __init__(self, resultat):
        self.resultat = resultat

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
        self.N = N
        self.B = B
        self.F = F
        self.connaissance = [(self.N, INCONNU, self.B)]

    def proposer(self):
        debug('--------------------')
        debug("Connaissance " + repr(self.connaissance))

        # S'il n'y a plus d'inconnu, on propose la solution
        if all(map(lambda t: t[2] == 0 or t[0] == t[2], self.connaissance)):
            i = 0
            resultat = []
            for (n, c, b) in self.connaissance:
                if b > 0:
                    resultat.extend([i + j for j in range(n)])
                i += n
            raise Resultat(" ".join([str(i) for i in resultat]))

        # On soumet un nouveau test.
        b = 0
        alternance = 0
        proposition = []


        for n, c, b in self.connaissance:
            debug("n=%d, c=%s, b=%d" % (n, c, b))
            if c == INCONNU:
                # Inconnu : On alterne tous les B bits ou demi-zone inconnue.
                # alternance = 1 - alternance
                demi = (n-1) / 2 + 1
                while n > 0:
                    m = min(b + 1, demi, n)
                    debug("m=%d, demi=%d" % (m, demi))
                    proposition.extend([alternance] * m)
                    n = n - m
                    if n>0:
                        alternance = 1 - alternance
            else:
                # Connu.
                proposition.extend([alternance] * n)

        # S'en souvenir pour recevoir()
        self.proposition = proposition
        return "".join([str(i) for i in proposition])

    def recevoir(self, reponse):
        i = 0
        prp = list(self.proposition)
        rep = list(reponse)
        newcon = []

        p = 0
        n = 0
        while len(self.connaissance) > 0 or n > 0:
            if p == 0:
                ref = prp[0]
                r = decompter(rep, ref)
                p = decompter(prp, ref)

                debug("ref = %s" % repr(ref))
                debug('prp = %s, p = %d' % (prp, p))
                debug('rep = %s, r = %d' % (rep, r))

                del prp[:p], rep[:r]

            if n == 0:
                n, c, b = self.connaissance.pop(0)
                debug("X n=%d, c=%s, b=%d" % (n, c, b))

            if r == p:
                x = min(n, p)
                newcon.append((x, OK, 0))
                p -= x
                n -= x
            else:  # r < p (et normalement p < b)
                if c == OK:
                    x = n
                    newcon.append((x, c, b))
                    n -= x
                    p -= x
                    r -= x
                elif c == HS:
                    x = n
                    newcon.append((x, c, b))
                    n -= x
                    p -= x
                    b -= x
                else:  # c == INCONNU
                    x = min(n, p)
                    bb = min(b, p - r)
                    debug('p=%d, r=%d, n=%d, b=%d, bb=%d' % (p, r, n, b, bb))
                    # if r == 0:
                    if bb <= 0 or b == 0:
                        newcon.append((x, OK, 0))
                        bb = 0
                    elif p - r > 0 and x != bb:
                        newcon.append((x, INCONNU, bb))
                    else:
                        newcon.append((x, HS, bb))
                        p = p + x
                    b -= bb
                    p -= x
                    n -= x

            debug(repr(newcon))

        self.connaissance = newcon


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
            try:
                proposition = resolveur.proposer()
                echo(proposition)
                rcv = readline()
                if rcv == "-1":
                    sys.exit(0)
            except Resultat as e:
                echo(e.resultat)
                rcv = readline()
                if rcv == "-1":
                    sys.exit(0)
                break

            resolveur.recevoir([int(c) for c in rcv])
    sys.exit(0)


if __name__ == '__main__':
    main()
