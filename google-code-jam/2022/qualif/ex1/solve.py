#!/usr/bin/python3


def resoudre(R, C):
    solution = [
        ".." + (C-1) * "+-" + "+",
        ".." + (C-1) * "|." + "|",
    ]

    type_1 = C * "+-" + "+"
    type_2 = C * "|." + "|"

    for r in range(R-1):
        solution.append(type_1)
        solution.append(type_2)

    solution.append(type_1)

    return solution


def main():
    T = int(input())
    for i in range(1, T + 1):
        R, C = [int(x) for x in input().split(' ')]
        solution = resoudre(R, C)
        print(f"Case #{i}:")
        for ligne in solution:
            print(ligne)

main()
