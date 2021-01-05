#!/usr/bin/python3


def lire(nom_fichier):
    programme = []
    with open(nom_fichier) as f:
        return [int(x) for x in f.readline().strip().split(",")]


def resoudre_1(liste, n=2020):
    tour = 0
    avant = {}
    memoire = {}
    for entier in liste:
        tour += 1
        if entier in memoire:
            avant[entier] = memoire[entier]
        memoire[entier] = tour

    while True:
        if tour == n:
            return entier
        entier = memoire[entier] - avant[entier] if entier in avant else 0

        tour += 1
        if entier in memoire:
            avant[entier] = memoire[entier]
        memoire[entier] = tour


def resoudre_2(programme):
    return resoudre_1(programme, 30000000)


def main():
    liste = lire("test")
    liste = lire("input")
    print(resoudre_1(liste))
    print(resoudre_2(liste))


main()

