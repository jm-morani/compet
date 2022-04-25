#!/usr/bin/python3

import sys
sys.setrecursionlimit(1500)


def resoudre(X, Y, S):
    optimal = float('inf')

    def chiffrer(x, y):
        if x == "C" and y == "J":
            return X
        elif x == "J" and y == "C":
            return Y
        return 0

    def parcourir(cout, i=0, x="", branche=False):
        nonlocal optimal

        if cout >= optimal:
            return

        if i >= len(S):
            if cout < optimal:
                optimal = cout
            return

        y = S[i]
        if y != "?":
            if branche:
                cout += chiffrer(x, y)
            parcourir(cout, i+1, y)
        else:
            parcourir(cout + chiffrer(x, "C"), i+1, "C", True)
            parcourir(cout + chiffrer(x, "J"), i+1, "J", True)

    cout = 0
    for i in range(1, len(S)):
        cout += chiffrer(S[i-1], S[i])
    parcourir(cout)

    return optimal


def main():
    T = int(input().strip())
    for i in range(1, T + 1):
        X, Y, S = input().strip().split(' ')
        solution = resoudre(int(X), int(Y), list(S))
        print(f"Case #{i}: {solution}")


main()

