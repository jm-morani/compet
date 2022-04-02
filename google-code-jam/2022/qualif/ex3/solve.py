#!/usr/bin/python3


def resoudre(dés):
    compte = 1
    for dé in sorted(dés):
        if compte <= dé:
            compte += 1
    return compte - 1


def main():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        dés = [int(dé) for dé in input().split(' ')]
        assert N == len(dés)
        solution = resoudre(dés)
        print(f"Case #{i}: {solution}")

main()
