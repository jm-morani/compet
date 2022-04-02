#!/usr/bin/python3


class Impossible(Exception):
    pass


def resoudre(imprimantes):
    objectif = 1000000
    solution = []

    while True:
        try:
            niveaux = [niveaux.pop(0) for niveaux in imprimantes]
        except IndexError:
            break
        qté_couleur = min(*niveaux, objectif)

        objectif -= qté_couleur
        solution.append(qté_couleur)

    if objectif > 0:
        raise Impossible()

    return solution


def main():
    T = int(input())
    for i in range(1, T + 1):
        imprimantes = [
            [int(niveau) for niveau in input().split(' ')]
            for _ in range(3)
        ]
        try:
            solution = resoudre(imprimantes)
            print(f"Case #{i}: {' '.join([str(couleur) for couleur in solution])}")
        except Impossible:
            print(f"Case #{i}: IMPOSSIBLE")

main()
