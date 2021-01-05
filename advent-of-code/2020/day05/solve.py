#!/usr/bin/python3


def lire(nom_fichier):
    return [ligne.strip() for ligne in open(nom_fichier)]


def resoudre_1(liste):
    return max([
        int(x.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), base=2)
        for x in liste
    ])


def resoudre_2(liste):
    liste = [
        int(x.replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1'), base=2)
        for x in liste
    ]
    for i in liste[:-1]:
        if i+1 not in liste and i+2 in liste:
            return i+1


def main():
    #jeu = lire("test")
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

