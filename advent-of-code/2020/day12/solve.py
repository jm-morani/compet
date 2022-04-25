#!/usr/bin/python3

EST = (1, 0)
NORD = (0, 1)
OUEST = (-1, 0)
SUD = (0, -1)

ABSOLU = {"E": EST, "N": NORD, "W": OUEST, "S": SUD}
DROITE = [EST, SUD, OUEST, NORD]
GAUCHE = list(reversed(DROITE))
RELATIF = {"L": GAUCHE, "R": DROITE}


def lire(nom_fichier):
    return [(ligne[0], int(ligne.strip()[1:])) for ligne in open(nom_fichier)]


def resoudre_1(directives):
    (x, y), orientation = (0, 0), (1, 0)

    for action, parametre in directives:
        if action == "F":
            x += orientation[0] * parametre
            y += orientation[1] * parametre
        elif action in ABSOLU:
            x += ABSOLU[action][0] * parametre
            y += ABSOLU[action][1] * parametre
        elif action in RELATIF:
            ordre = RELATIF[action]
            quarts = (ordre.index(orientation) + parametre // 90) % 4
            orientation = ordre[quarts]
    return abs(x) + abs(y)


def resoudre_2(directives):
    pass


def main():
    jeu = lire("test")
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

