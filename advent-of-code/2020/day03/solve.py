#!/usr/bin/python3
from sys import stdin


class Piste:
    def __init__(self, lignes):
        self.lignes = lignes
        self.hauteur = len(lignes)
        self._largeur = len(lignes[0])

    def get(self, x, y):
        #print((x,y))
        return self.lignes[y][x % self._largeur]


def lire(nom_fichier):
    lignes = [ligne.strip() for ligne in open(nom_fichier)]
    return Piste(lignes)


def resoudre_1(piste, X=3, Y=1):
    n = 0
    x, y = 0, 0
    while y < piste.hauteur-1:
        x += X
        y += Y
        if piste.get(x, y) == "#":
            n += 1
    return n


def resoudre_2(piste):
    return 1 * \
        resoudre_1(piste, 1, 1) * \
        resoudre_1(piste, 3, 1) * \
        resoudre_1(piste, 5, 1) * \
        resoudre_1(piste, 7, 1) * \
        resoudre_1(piste, 1, 2)


def main():
    jeu = lire("test")
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()
