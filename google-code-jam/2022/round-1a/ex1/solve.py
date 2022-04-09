#!/usr/bin/python3


def parcourir(S):
    S += '@'
    lettre, nb = S[0], 1
    for suivante in S[1:]:
        if lettre == suivante:
            nb += 1
        else:
            yield lettre, nb, suivante
            lettre, nb = suivante, 1


def resoudre(S):
    solution = ''

    for lettre, nb, suivante in parcourir(S):
        if lettre < suivante:
            solution += 2 * nb * lettre
        else:
            solution += nb * lettre

    return solution


def main():
    T = int(input())
    for i in range(1, T + 1):
        S = input().strip()
        solution = resoudre(S)
        print(f"Case #{i}: {solution}")

main()
