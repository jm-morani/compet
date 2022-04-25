#!/usr/bin/python3


def resoudre(P, R):
    moyenne = sum([sum(r) for r in R]) / 10000

    qR = zip(*R)

    faciles, difficiles = [0] * 100, [0] * 100
    for correctes in qR:
        categorie = faciles if sum(correctes) > moyenne else difficiles
        for joueur, correcte in enumerate(correctes):
            categorie[joueur] += correcte
    
    suspect, min_ecart = None, float('inf')
    for joueur in range(100):
        ecart = faciles[joueur] - difficiles[joueur]
        if ecart < min_ecart:
            suspect, min_ecart = joueur, ecart

    return suspect


def main():
    T = int(input())
    P = int(input())
    for i in range(1, T + 1):
        R = [[int(r) for r in input()] for _ in range(100)]
        solution = resoudre(P, R)
        print(f"Case #{i}: {solution+1}")


main()

