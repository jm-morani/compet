#!/usr/bin/python3


def lire():
    return input()


def resoudre_1(jeu):
    chaine = jeu[:4]
    for i, c in enumerate(jeu[4:]):
        chaine = chaine[1:] + c
        if len(set(chaine)) == 4:
            return i + 5


def resoudre_2(jeu):
    chaine = jeu[:14]
    for i, c in enumerate(jeu[14:]):
        chaine = chaine[1:] + c
        if len(set(chaine)) == 14:
            return i + 15


def main():
    jeu = lire()
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

