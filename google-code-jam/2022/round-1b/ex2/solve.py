#!/usr/bin/python3


def resoudre(N, P, clients):
    # Gauche : (Où je suis, mon cout) + Droite : (Où je suis, mon coût)
    départs = [[0, 0], [0, 0]]
    for client in clients:
        gauche, droite = min(client), max(client)

        cout_gauche_droite = abs(départs[0][0] - gauche) + départs[0][1]
        cout_gauche_gauche = abs(départs[0][0] - droite) + départs[0][1]
        cout_droite_droite = abs(départs[1][0] - gauche) + départs[1][1]
        cout_droite_gauche = abs(départs[1][0] - droite) + départs[1][1]

        fixe = droite - gauche
        cout_gauche = min(cout_gauche_gauche, cout_droite_gauche) + fixe
        cout_droite = min(cout_gauche_droite, cout_droite_droite) + fixe

        départs = [[gauche, cout_gauche], [droite, cout_droite]]

    return min(départs[0][1], départs[1][1])


def main():
    T = int(input())
    for i in range(1, T + 1):
        N, P = [int(x) for x in input().split(' ')]
        clients = [
            [int(x) for x in input().split(' ')]
            for n in range(N)
        ]
        solution = resoudre(N, P, clients)
        print(f"Case #{i}: {solution}")

main()
