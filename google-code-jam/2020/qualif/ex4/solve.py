#!/usr/bin/python3


def resoudre(B):
    nb_lectures = 0
    mystere = [None] * B

    def lire(position):
        nonlocal nb_lectures
        nb_lectures += 1
        print(position + 1, flush=True)
        res =  bool(int(input()))
        return res

    def resynchroniser():
        transformation = {}

        def traiter(g):
            d = B - g - 1
            nonlocal transformation
            egaux = mystere[g] == mystere[d]
            if egaux not in transformation:
                transformation[egaux] = mystere[g] == lire(g)
            mystere[g] = mystere[g] == transformation[egaux]
            mystere[d] = egaux == mystere[g]

        for i in range(B // 2):
            traiter(i)
        if len(transformation) == 1:
            pour_garder_la_parite = lire(0)

    def Parcours():
        gauche, droite = 0, 0
        while gauche + droite < B:
            if gauche <= droite:
                yield gauche
                gauche += 1
            else:
                yield B - droite - 1
                droite += 1

    for position in Parcours():
        if nb_lectures % 10 == 0 and nb_lectures > 0:
            resynchroniser()
        mystere[position] = lire(position)

    return ''.join(['1' if n else '0' for n in mystere])


def main():
    T, B = [int(x) for x in input().split(' ')]
    for i in range(1, T + 1):
        solution = resoudre(B)
        print(solution, flush=True)
        assert(input() == 'Y')


main()
