#!/usr/bin/python3

from math import lcm as ppcm


def lire(nom_fichier):
    with open(nom_fichier) as f:
        timestamp = int(f.readline())
        horaires = [int(i) if i != "x" else None for i in f.readline().split(",")]
    return (timestamp, horaires)


def resoudre_1(timestamp, horaires):
    meilleur, bus = None, None
    horaires = [h for h in horaires if h is not None]

    for h in horaires:
        attente = (h - timestamp % h) % h
        if meilleur is None or attente < meilleur:
            meilleur, bus = attente, h

    return meilleur * bus


def resoudre_2(timestamp, horaires):
    horaires = [(h, d) for (d, h) in enumerate(horaires) if h is not None]

    m, n = 1, 0
    for h, d in horaires:
        for i in range(h):
            if (n + i*m + d) % h == 0:
                n += i*m
                break
        m = ppcm(m, h)

    for h, d in horaires:
        if (n + d) % h != 0:
            print(f"err {h=}, {d=}")

    return n


def main():
    timestamp, horaires = lire("test") # 295, 1068781
    timestamp, horaires = lire("input")
    print(resoudre_1(timestamp, horaires))
    print(resoudre_2(timestamp, horaires))


main()

