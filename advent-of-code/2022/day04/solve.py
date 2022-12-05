#!/usr/bin/python3
from sys import stdin
from collections import namedtuple

Intervalle = namedtuple("Intervalle", ["début", "fin"])


def lire():
    return [
        tuple(
            Intervalle(*(
                int(x)
                for x in interval.split('-', 1)
            ))
            for interval in ligne.strip().split(',', 1)
        )
        for ligne in stdin
    ]


def resoudre_1(jeu):
    total = 0
    for (elf1, elf2) in jeu:
        if elf1.début <= elf2.début and elf2.fin <= elf1.fin or \
           elf2.début <= elf1.début and elf1.fin <= elf2.fin:
            total += 1
    return total


def resoudre_2(jeu):
    total = 0
    for (elf1, elf2) in jeu:
        if elf1.début <= elf2.début <= elf1.fin or \
           elf2.début <= elf1.début <= elf2.fin:
            total += 1
    return total


def main():
    jeu = lire()
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()
