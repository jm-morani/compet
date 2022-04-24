#!/usr/bin/python3


def resoudre(D):
    paiement = 0
    précédent = -1

    début, fin = 0, len(D) - 1
    while début <= fin:
        if D[début] < D[fin]:
            pancake = D[début]
            début += 1
        else:
            pancake = D[fin]
            fin -= 1
        if pancake >= précédent:
            paiement += 1
            précédent = max(précédent, pancake)

    return paiement


def main():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        D = [int(x) for x in input().split(' ')]
        assert len(D) == N
        solution = resoudre(D)
        print(f"Case #{i}: {solution}")

main()
