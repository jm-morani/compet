#!/usr/bin/python3


from random import shuffle


def resoudre(N, K):
    premiere, passages = [int(f) for f in input().split(' ')]
    vus = passages  # Double de la différence par rapport au graphe minimal
    manquant = (N - 1) - passages # Double de la différence par rapport au graphe complet

    échantillon = list(range(1, N+1))
    échantillon.pop(premiere - 1)
    shuffle(échantillon)
    échantillon = échantillon[:K]

    for suivante in échantillon:
        print(f"T {suivante}", flush=True)
        _, passages = [int(f) for f in input().split(' ')]
        vus += passages
        manquant += (N - 1) - passages

    # Extrapolation
    projection = (N * manquant) / (len(échantillon) + 1)
    estimation = int((N * (N - 1) - projection - 1) // 2)

    # Bornage
    minimum = (vus + (N - (len(échantillon) + 1)) + 1) // 2
    minimum *= (4 / 3)
    minimum = int(minimum)
    estimation = max(estimation, minimum)

    maximum = (N * (N - 1) - manquant) // 2
    maximum *= (2 / 3)
    maximum = int(maximum) if maximum == int(maximum) else int(maximum+1)
    estimation = min(estimation, maximum)

    print(f"E {estimation}", flush=True)


def main():
    T = int(input())
    for _ in range(1, T + 1):
        N, K = [int(f) for f in input().split(' ')]
        resoudre(N, K)


main()
