#!/usr/bin/python3
from sys import stdin



def lire(nom_fichier):
    return [
        int(ligne.strip())
        for ligne in open(nom_fichier)
    ]


def resoudre_1(entiers):
    entiers = sorted(entiers)
    while entiers:
        x = entiers.pop(0)
        for y in entiers:
            somme = x + y
            if somme > 2020:
                break
            if somme == 2020:
                return x * y


def resoudre_2(entiers):
    entiers = sorted(entiers)
    longueur = len(entiers)
    for i in range(0, longueur):
        x = entiers[i]
        if x + x + x > 2020:
            break
        for j in range(i+1, longueur):
            y = entiers[j]
            if x + y + y > 2020:
                break
            for k in range(j+1, longueur):
                z = entiers[k]
                somme = x + y + z
                if somme > 2020:
                    break
                if somme == 2020:
                    return x * y * z


def main():
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()
