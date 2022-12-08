#!/usr/bin/python3
from sys import stdin
from collections import namedtuple


Commande = namedtuple("Commande", ["instruction", "résultat"])
Répertoire = namedtuple("Répertoire", ["nom"])
Fichier = namedtuple("Fichier", ["nom", "taille"])


def lire():
    commandes = []

    instruction, résultat = None, []
    for ligne in stdin:
        ligne = ligne.strip("\r\n")
        if ligne.startswith("$"):
            if instruction:
                commandes.append(Commande(instruction, résultat))
            instruction = ligne[1:].strip().split(' ')
            résultat = []
        else:
            tokens = ligne.split(" ")
            élément = Répertoire(tokens[1]) \
                if tokens[0] == "dir" \
                else Fichier(tokens[1], int(tokens[0]))
            résultat.append(élément)

    if instruction:
        commandes.append(Commande(instruction, résultat))

    return commandes


def construire(jeu):
    racine = {}
    courant = {} 
    for instruction, résultat in jeu:
        if instruction[0] == "cd":
            chemin = instruction[1] 
            if chemin == "/":
                courant = racine
            elif chemin != ".":
                if chemin not in courant:
                    courant[chemin] = {}
                courant = courant[chemin]
        elif instruction[0] == "ls":
            for élément in résultat:
                if isinstance(élément, Répertoire):
                    if élément.nom not in courant:
                        courant[élément.nom] = {"..": courant}
                elif isinstance(élément, Fichier):
                    courant[élément.nom] = élément.taille
    return racine


def sommer(répertoire, visiteur):
    somme = 0
    for nom, valeur in répertoire.items():
        if isinstance(valeur, dict):
            if nom != "..":
                somme += sommer(valeur, visiteur)
        else:
            somme += valeur
    visiteur(somme)
    return somme


def resoudre_1(jeu):
    racine = construire(jeu)
    résultat = 0 
    def visiteur(taille):
        nonlocal résultat
        if taille <= 100000:
            résultat += taille
    sommer(racine, visiteur)
    return résultat


def resoudre_2(jeu):
    racine = construire(jeu)
    candidats = []
    taille_racine = sommer(racine, candidats.append)
    besoin = 30000000 - (70000000 - taille_racine)
    candidats.sort()
    for candidat in candidats:
        if candidat >= besoin:
            return candidat


def main():
    jeu = lire()
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

