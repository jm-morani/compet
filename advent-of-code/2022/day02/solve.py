#!/usr/bin/python3
from sys import stdin

PAPIER = 2
CAILLOU = 1
CISEAUX = 3

traduction = {
    'B': PAPIER, 'A': CAILLOU, 'C': CISEAUX,
    'Y': PAPIER, 'X': CAILLOU, 'Z': CISEAUX,
}

def lire(nom_fichier):
    jeu = []
    for ligne in open(nom_fichier):
        jeu.append([x for x in ligne.strip().split(' ')])
    return jeu


def resoudre_1(jeu):
    possibilités = {
        'A': {'X': 1 + 3, 'Y': 2 + 6, 'Z': 3 + 0},
        'B': {'X': 1 + 0, 'Y': 2 + 3, 'Z': 3 + 6},
        'C': {'X': 1 + 6, 'Y': 2 + 0, 'Z': 3 + 3},
    }
    return sum([
        possibilités[lui][moi]
        for (lui, moi) in jeu
    ])


def resoudre_2(jeu):
    possibilités = {
        'A': {'X': 3 + 0, 'Y': 1 + 3, 'Z': 2 + 6},
        'B': {'X': 1 + 0, 'Y': 2 + 3, 'Z': 3 + 6},
        'C': {'X': 2 + 0, 'Y': 3 + 3, 'Z': 1 + 6},
    }
    return sum([
        possibilités[lui][moi]
        for (lui, moi) in jeu
    ])
    
def main():
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()
