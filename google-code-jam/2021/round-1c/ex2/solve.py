#!/usr/bin/python3

from random import randint
import math
infini = math.inf


DEBUG = False


def plus_petit(valeurs):
    minimum, index = valeurs[0], 0
    for i, valeur in enumerate(valeurs):
        if valeur < minimum:
            minimum, index = valeur, i
    return minimum, index


def fusionner(générateurs):
    valeurs = [next(générateur, infini) for générateur in générateurs]
    while True:
        valeur, index = plus_petit(valeurs)
        yield valeur
        valeurs[index] = next(générateurs[index], infini)


def infrange(initiale):
    while True:
        yield initiale
        initiale += 1


def générer(Y, longueur):
    référence_initiale = int(str(Y)[:longueur])

    def xgénérer(initiale):
        for référence in infrange(initiale):
            hypothèse = str(référence)
            référence += 1
            hypothèse += str(référence)
            while int(hypothèse) <= Y:
                référence += 1
                hypothèse += str(référence)
            if DEBUG:
                print(f"-- {longueur} {initiale} -- ", hypothèse, "    <---" if hypothèse == DEBUG else "")
            yield int(hypothèse)

    générateurs = [xgénérer(référence_initiale)]
    générateurs.append(xgénérer(référence_initiale + 1))
    #for i in range(1, len(str(référence_initiale))):
    #    m = int(i * "9")
    #    if DEBUG:
    #        print(m)
    #    générateurs.append(xgénérer(m))
    #    m *= 10
    return fusionner(générateurs)

    
def resoudre(Y):
    générateurs = [générer(Y, l) for l in range(1, len(str(Y)) + 1)]
    return next(fusionner(générateurs))


def test():
    for i in range(10000):
        l = randint(2,5)
        x = randint(1,1000)
        z = int("".join([str(n) for n in range(x, x+l)]))
        y = z - randint(1, 10000)
        if y < 1:
            continue

        r = resoudre(y)
        if r > z:
            print(f"{y=}, {z=} ==> {r=}")
            global DEBUG
            DEBUG = z
            resoudre(y)
            return


def main():
    test()
    return
    T = int(input().strip())
    for x in range(1, T + 1):
        Y = int(input())
        z = resoudre(Y)
        print(f"Case #{x}: {z}")


if __name__ == "__main__":
    main()

