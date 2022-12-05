#!/usr/bin/python3
from sys import stdin


def lire(nom_fichier):
    elfes = []
    nourritures = []
    for ligne in open(nom_fichier):
        ligne = ligne.strip()
        if ligne:
            nourritures.append(int(ligne))
        else:
            elfes.append(nourritures)
            nourritures = []
    elfes.append(nourritures)
    return elfes


def resoudre_1(jeu):
    return max([
        sum(nourritures)
        for elf, nourritures in enumerate(jeu)
    ])


def resoudre_2(jeu):
    liste = sorted([
        sum(nourritures)
        for elf, nourritures in enumerate(jeu)
    ])
    return sum(liste[-3:])
    

def main():
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()
