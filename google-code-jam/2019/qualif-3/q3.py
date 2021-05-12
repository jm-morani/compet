#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
from math import sqrt
from random import choice, shuffle
from fractions import gcd
from traceback import print_exc


def calculer(N, liste):
    """
    Renvoie la liste des entiers premiers
    de la liste originale
    """
    x, y, liste = liste[0], liste[1], liste[1:]
    
    if x == y:
        resultat = calculer(N, liste)
        b = resultat[0]
        resultat.insert(0, x / b)
        return resultat
    
    b = gcd(x, y)
    a = x / b
    resultat = [a, b]
    while len(liste) > 0:
        y = liste.pop(0)
        c = y / b
        resultat.append(c)
        b = c
    return resultat


def resoudre(N, liste):
    """
    Effectue un simple traitement alphabetique
    """
    resolu = calculer(N, liste)
    tried = sorted(set(resolu))
    resultat = ''
    for x in resolu:
        resultat += chr(65+tried.index(x))
    return resultat


def calculer_liste_de_premiers(N):
    resultat = [2]
    for n in xrange(3, N):
        limite = int(sqrt(n))
        for d in resultat:
            if d > limite:
                continue # Pas terrible, suffisant pour tests
            if n % d == 0:
                break
        else:
            resultat.append(n)
    return resultat


def test():
    # Precalcule des nombres premiers
    premiers = calculer_liste_de_premiers(100000)
    
    for essai in xrange(9999):
        # Choix des valeurs de substitution
        choix = set()
        while len(choix) < 26:
            choix.add(choice(premiers))
        choix = sorted(list(choix))
        
        # Majorant (que l'on utilisera pas)
        majorant = max(choix) + 1
        
        # Texte clair
        # texte = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        texte = list("ABCDEFGHIJKLMNOPQRSTUVWXYZAAABBBZZZ")
        shuffle(texte)
        texte = ''.join(texte)
        
        # "Chiffrement"
        echantillon = []
        a = 0
        for lettre in texte:
            b = choix[ord(lettre) - 65]
            echantillon.append(a*b)
            a = b
        echantillon.pop(0)
        
        # Test
        try:
            resultat = resoudre(majorant, echantillon)
            texte = ''.join(texte)
            if resultat != texte:
                print "ECHEC : %s / %s" % (texte, resultat)
                print echantillon
                print "------------------------------------"
        except:
            print "ECHEC : %s" % texte
            print echantillon
            print_exc()
            print "------------------------------------"


def main():
    T = int(sys.stdin.readline())
    for i in xrange(1, T+1):
        N, L = [int(x) for x in sys.stdin.readline().split(' ')]
        liste = [int(x) for x in sys.stdin.readline().split(' ')]
        res = resoudre(N, liste)
        print "Case #%d: %s" % (i, res)


if __name__ == '__main__':
    if 'test' in sys.argv:
        test()
    else:
        main()
