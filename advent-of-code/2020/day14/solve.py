#!/usr/bin/python3

import re

MASK = re.compile("^mask = ([01X]+)$")
MEM = re.compile("^mem\\[(\\d+)\\] = (\d+)$")


def lire(nom_fichier):
    programme = []
    for ligne in open(nom_fichier):
        m = MASK.match(ligne)
        if m:
            programme.append((m.group(1),))
            continue

        m = MEM.match(ligne)
        if m:
            programme.append((int(m.group(1)), int(m.group(2))))
            continue
    return programme


def resoudre_1(programme):
    memoire, zeros, uns = {}, 0, 0
    for instruction in programme:
        if len(instruction) == 1:
            (chaine, ) = instruction
            zeros = int(chaine.replace("X", "1"), base=2)
            uns = int(chaine.replace("X", "0"), base=2)
        else:
            (adresse, valeur) = instruction
            memoire[adresse] = valeur & zeros | uns
    return sum(memoire.values())


def resoudre_2(programme):
    def Possibilites(masque, adresse):
        adresse = f"{adresse:b}".zfill(len(masque))
        adresse = "".join([
            a if m == "0" else m
            for m, a in zip(masque, adresse)
        ])
        n = adresse.count("X")
        parties = adresse.split("X")
        for i in range(2**n):
            resultat = parties[0]
            for j, partie in enumerate(parties[1:]):
                resultat += ("1" if i & 2**j else "0") + partie
            yield int(resultat, base=2)

    memoire = {}
    for instruction in programme:
        if len(instruction) == 1:
            (masque, ) = instruction
        else:
            (original, valeur) = instruction
            for adresse in Possibilites(masque, original):
                memoire[adresse] = valeur
    return sum(memoire.values())


def main():
    programmes = lire("test"), lire("test2")
    programmes = lire("input"), lire("input")
    print(resoudre_1(programmes[0]))
    print(resoudre_2(programmes[1]))


main()

