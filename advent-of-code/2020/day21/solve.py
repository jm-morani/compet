#!/usr/bin/python3

from itertools import chain
from collections import defaultdict


def lire(nom_fichier):
    produits = []
    for ligne in open(nom_fichier):
        ligne = ligne.strip().replace(",", "").replace("(", "").replace(")", "")
        ingredients, allergenes = ligne.split(" contains ", 1)
        produits.append((set(ingredients.split(" ")), set(allergenes.split(" "))))
    return produits


def identifier(candidats, coupables):
    if not candidats:
        return True

    ingredient = list(candidats.keys())[0]
    allergenes_original = candidats[ingredient]
    allergenes = allergenes_original - set(coupables.values())

    del candidats[ingredient]
    for allergene in allergenes:
        coupables[ingredient] = allergene
        ok = identifier(candidats, coupables)
        if ok:
            return ok
        del coupables[ingredient]
    candidats[ingredient] = allergenes_original
    return False


def resoudre(produits):
    tous_allergenes = set()
    tous_ingredients = set()
    candidats = defaultdict(set)
    frequence = defaultdict(int)

    for ingredients, allergenes in produits:
        tous_allergenes |= allergenes
        tous_ingredients |= ingredients
        for allergene in allergenes:
            candidats[allergene] |= ingredients
        for ingredient in ingredients:
            frequence[ingredient] += 1

    for ingredients, allergenes in produits:
        for allergene in allergenes:
            candidats[allergene] -= (tous_ingredients - ingredients)

    suspects = set(chain.from_iterable(candidats.values()))
    sains = tous_ingredients - suspects
    print(sum([frequence[ingredient] for ingredient in sains]))

    coupables = dict()
    identifier(candidats, coupables)
    print(",".join([c[1] for c in sorted(coupables.items())]))


def main():
    produits = lire("test")
    produits = lire("input")
    resoudre(produits)


main()

