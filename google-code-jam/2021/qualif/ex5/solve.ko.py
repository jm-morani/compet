#!/usr/bin/python3
from math import sqrt

def div(dividende, diviseur):
    return dividende/diviseur if dividende else 0

def resoudre(P, R):
    #moyenne = sum([sum(r) for r in R]) / 10000

    qR = zip(*R)

    # On classe les questions en niveau de difficulté (0..100)
    difficultes_j = [[0] * (100+1) for _ in range(100)]
    difficultes_t = [0] * (100+1)
    difficultes_n = [0] * (100+1)
    for correctes in qR:
        niveau = sum(correctes)
        somme = 0
        for joueur, correcte in enumerate(correctes):
            somme += correcte
            difficultes_j[joueur][niveau] += correcte
        difficultes_n[niveau] += 1
        difficultes_t[niveau] += somme

    # Moyenne par niveau de difficulté
    moyennes_tous = [
        div(difficultes_t[niveau], difficultes_n[niveau]) / 100
        for niveau in range(100+1)
    ]
    # Moyenne par niveau de chaque joueur
    moyennes_joueurs = [
        [
            div(difficultes_j[joueur][niveau], difficultes_n[niveau])
            for niveau in range(100+1)
        ]     
        for joueur in range(100)
    ]

    suspect, max_variance = None, 0
    for joueur, moyennes in enumerate(moyennes_joueurs):
        variance = 0
        for niveau in range(100+1):
            ecart = moyennes_tous[niveau] - moyennes[niveau]
            ecart = ecart if ecart > 0 else -ecart
            variance += sqrt(ecart) if ecart else 0
        print(joueur, variance)
        if variance > max_variance:
            suspect, max_variance = joueur, variance

    return suspect


def main():
    T = int(input())
    P = int(input())
    for i in range(1, T + 1):
        R = [[int(r) for r in input()] for _ in range(100)]
        solution = resoudre(P, R)
        print(f"Case #{i}: {solution+1}")


main()

