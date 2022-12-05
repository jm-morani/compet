#!/usr/bin/python3
from sys import stdin


def priorité(objet):
    return ord(objet) - 96 if 'a' <= objet <= 'z' else ord(objet) - 38


def lire(nom_fichier):
    sacs = []
    for ligne in open(nom_fichier):
        ligne = ligne.strip()
        sacs.append(ligne)
    return sacs


def resoudre_1(jeu):
    total = 0
    for sac in jeu:
        compartiment_1 = set(sac[:len(sac)//2])
        compartiment_2 = set(sac[len(sac)//2:])
        commun = compartiment_1 & compartiment_2
        for obj in commun:
            total += priorité(obj)
    return total


def resoudre_2(jeu):
    total = 0
    i = iter(jeu)
    try:
        while True:
            sac_1 = set(next(i))
            sac_2 = set(next(i))
            sac_3 = set(next(i))
            commun = sac_1 & sac_2 & sac_3
            for obj in commun:
                total += priorité(obj)
    except StopIteration:
        pass
    return total
    

def main():
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()
