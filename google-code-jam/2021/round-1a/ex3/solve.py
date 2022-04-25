#!/usr/bin/python3

# Marchera pas pour le troisième test set, car il y aura mieux à faire.


def resoudre(N, Q, L):
    # Sous la moyenne (la moitié du score max), on inverse
    moyenne = Q / 2
    L = [
        (a, s)
        if s > moyenne
        else (a.replace("T", "X").replace("F", "T").replace("X", "F"), Q-s)
        for a, s in L
    ]

    # On recopie tout simplement le meilleur.
    A = "T" * Q
    S = 0
    for (a, s) in L:
        if s > S:
            A, S = a, s

    return A, S


def main():
    T = int(input())
    for i in range(1, T + 1):
        N, Q = [int(x) for x in input().split(' ')]
        L = []
        for _ in range(N):
            a, s = input().split(' ')
            L.append((a, int(s)))
        A, S = resoudre(N, Q, L)
        print(f"Case #{i}: {A} {S}/1")


if __name__ == "__main__":
    main()
