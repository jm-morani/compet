#!/usr/bin/python3

# TOUT JUSTE BON POUR LE PREMIER NIVEAU


def resoudre():
    N = 1
    while N not in (-1, 0):
        print((N * "1") + (8-N) * "0", flush=True)
        N = int(input())


def main():
    T = int(input())
    for _ in range(T):
        resoudre()


main()
