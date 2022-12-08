#!/usr/bin/python3
from sys import stdin
from collections import namedtuple


def lire():
    return [
        [
            int(taille)
            for taille in ligne.strip()
        ]
        for ligne in stdin
    ]


def nord(jeu, i, j):
    while i > 0:
        i -= 1
        yield jeu[i][j]

def sud(jeu, i, j):
    limite = len(jeu) - 1
    while i < limite:
        i += 1
        yield jeu[i][j]

def est(jeu, i, j):
    while j > 0:
        j -= 1
        yield jeu[i][j]

def ouest(jeu, i, j):
    limite = len(jeu[0]) - 1
    while j < limite:
        j += 1
        yield jeu[i][j]


def resoudre_1(jeu):
    def visible(parcours):
        for autre in parcours:
            if autre >= arbre:
                return False
        return True

    compteur = 0
    for i, rangée in enumerate(jeu):
        for j, arbre in enumerate(rangée):
            if visible(nord(jeu, i, j)) or \
               visible(sud(jeu, i, j)) or \
               visible(est(jeu, i, j)) or \
               visible(ouest(jeu, i, j)):
                compteur += 1
    return compteur


def resoudre_2(jeu):
    def visibilité(parcours):
        compteur = 0
        for autre in parcours:
            compteur += 1
            if autre >= arbre:
                break
        return compteur 

    max_score = 0
    for i, rangée in enumerate(jeu):
        for j, arbre in enumerate(rangée):
            score = visibilité(nord(jeu, i, j)) \
                    * visibilité(sud(jeu, i, j)) \
                    * visibilité(est(jeu, i, j)) \
                    * visibilité(ouest(jeu, i, j))
            if score > max_score:
                max_score = score
    return max_score


def main():
    jeu = lire()
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

