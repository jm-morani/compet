#!/usr/bin/python3

# MARCHE PAS EN L'ETAT

from sys import stderr

def resoudre(N):
    mien = [str(2**n) for n in range(N)]
    print(f"{' '.join(mien)}", flush=True)
    print(f"{' '.join(mien)}", file=stderr, flush=True)

    print("J", input().split(' '), file=stderr, flush=True)
    autres = [int(s) for s in input().split(' ')]
    print(autres, file=stderr, flush=True)

    A, B = 0, 0
    solution = []
    for x in reversed(sorted(autres)):
        print(x, file=stderr, flush=True)
        if A < B:
            A += x
            solution.append(x)
        else:
            B += x

    print(A, file=stderr, flush=True)
    print(B, file=stderr, flush=True)
    print(solution, file=stderr, flush=True)

    print(f"{' '.join(mien)}", flush=True)


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        resoudre(N)


main()
