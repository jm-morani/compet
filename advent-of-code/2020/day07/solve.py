#!/usr/bin/python3

from collections import defaultdict


# light red bags contain 1 bright white bag, 2 muted yellow bags.
# faded blue bags contain no other bags.
def lire(nom_fichier):
    regles = {}
    for ligne in open(nom_fichier):
        ligne = ligne.strip().replace(".", "").replace(" bags", "").replace(" bag", "").replace(" contains ", " contain ")
        contenant, reste = ligne.split(" contain ")
        contenu = {}
        if reste !=  "no other":
            for x in reste.split(", "):
                qte, couleur = x.split(" ", 1)
                contenu[couleur] = int(qte)
        regles[contenant] = contenu
    return regles


def resoudre_1(regles):
    inversion = defaultdict(set)
    for contenant, contenus in regles.items():
        for contenu in contenus:
            inversion[contenu] |= set((contenant,))

    def parcourir(resultat, depart):
        contenants = inversion[depart]
        for contenant in contenants:
            if contenant not in resultat:
                resultat |= set((contenant, ))
                parcourir(resultat, contenant)

    resultat = set()
    parcourir(resultat, "shiny gold")
    return len(resultat)


def resoudre_2(regles):
    cache = {}

    def compter(contenant):
        if contenant in cache:
            return cache[contenant]

        n = 1
        contenus = regles[contenant]
        for contenu, nombre in contenus.items():
            n += nombre * compter(contenu)

        cache[contenant] = n
        return n

    return compter("shiny gold") - 1


def main():
    jeu = lire("test")
    jeu = lire("test2")
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

