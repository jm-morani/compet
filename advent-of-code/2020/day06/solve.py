#!/usr/bin/python3

import re


def lire(nom_fichier):
    groupes = []
    groupe = []
    for ligne in open(nom_fichier):
        ligne = ligne.strip()
        if ligne:
            groupe.append(ligne)
        else:
            groupes.append(groupe)
            groupe = []
    groupes.append(groupe)
    return groupes


def resoudre_1(groupes):
    n = 0
    for groupe in groupes:
        answers = ""
        for individu in groupe:
            answers += individu
        n += len(set(answers))
    return n


def resoudre_2(groupes):
    n = 0
    for groupe in groupes:
        answers = ""
        for individu in groupe:
            answers += individu
        for x in set(answers):
            if answers.count(x) == len(groupe):
                n += 1
    return n


def main():
    jeu = lire("test")
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

