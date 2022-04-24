#!/usr/bin/python3

from sys import stderr


def suivre(anciennes, réponse, N):
    nouvelles = set()
    for ancienne in anciennes:
        for r in range(8):
            w = réponse[r:] + réponse[:r]
            nouvelle = "".join('1' if w[i] != ancienne[i] else '0' for i in range(8))
            # print(f"{ancienne=}, {r=}, {nouvelle=}", file=stderr, flush=True)
            if nouvelle.count("1") == N:
                nouvelles.add(nouvelle)
    return nouvelles


def resoudre():
    N = 1
    possibilités = set(f"{i:08b}" for i in range(256))

    while N not in (-1, 0):
        réponse = list(possibilités)[-1]
        print(réponse, flush=True)
        N = int(input())
        # print(f"{réponse=} {N=}", file=stderr, flush=True)
        possibilités = suivre(possibilités, réponse, N)


def main():
    T = int(input())
    for _ in range(T):
        resoudre()


main()
