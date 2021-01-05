#!/usr/bin/python3
from sys import stdin


def lire(nom_fichier):
    res = []
    for ligne in open(nom_fichier):
        ligne = ligne.strip()
        if ligne:
            (contrainte, chaine) = ligne.split(":", 1)
            minmax, caractere = contrainte.split(" ", 1)
            mi, ma = [int(x) for x in minmax.split("-", 1)]
            res.append((caractere, mi, ma, chaine.strip()))
    return res


def resoudre_1(jeu):
    n = 0
    for (caractere, mi, ma, chaine) in jeu:
        if mi <= chaine.count(caractere) <= ma:
            n += 1
    return n


def resoudre_2(jeu):
    n = 0
    for (caractere, mi, ma, chaine) in jeu:
        if (chaine[mi-1] == caractere) != (chaine[ma-1] == caractere):
            n += 1
    return n

def main():
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()
