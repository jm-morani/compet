#!/usr/bin/python3

CONNEXES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def lire(nom_fichier):
    return [ligne.strip() for ligne in open(nom_fichier)]


class Plan:
    def __init__(self, entree):
        if isinstance(entree, Plan):
            self.donnees = [x[:] for x in entree.donnees]
        else:  # brut
            self.donnees = [list(x) for x in zip(*entree)]
        self.largeur = len(self.donnees)
        self.hauteur = len(self.donnees[0])

    def nb_occupees(self, x, y):
        resultat = 0
        for (dx, dy) in CONNEXES:
            xx, yy = x + dx, y + dy
            if not (0 <= xx < self.largeur and 0 <= yy < self.hauteur):
                continue
            if self.donnees[xx][yy] == "#":
                resultat += 1
        return resultat

    def nb_occupees_2(self, x, y):
        resultat = 0
        for (dx, dy) in CONNEXES:
            for i in range(1, max(self.hauteur, self.largeur)):
                xx, yy = x + i * dx, y + i * dy
                if not (0 <= xx < self.largeur and 0 <= yy < self.hauteur):
                    break
                if self.donnees[xx][yy] == "L":
                    break
                # print(i, x, y, xx, yy)
                if self.donnees[xx][yy] == "#":
                    resultat += 1
                    break
        return resultat

    def compter(self, etats):
        resultat = 0
        for i in range(self.largeur):
            for j in range(self.hauteur):
                if self.donnees[i][j] in etats:
                    resultat += 1
        return resultat

    def clone(self):
        return Plan(self)

    def __getitem__(self, i):
        return self.donnees[i]

    def __eq__(self, other):
        return other is not None and self.donnees == other.donnees

    def __str__(self):
        aaa = [list(x) for x in zip(*self.donnees)]
        return "\n" + "\n".join(["".join(x) for x in aaa])


def resoudre_1(donnees):
    ancien, nouveau = None, Plan(donnees)

    while nouveau != ancien:
        ancien = nouveau.clone()

        for x in range(ancien.largeur):
            for y in range(ancien.hauteur):
                if ancien[x][y] != ".":
                    nb_places_occupees = ancien.nb_occupees(x, y)
                    if nb_places_occupees == 0:
                        nouveau[x][y] = "#"
                    elif nb_places_occupees >= 4:
                        nouveau[x][y] = "L"
    return nouveau.compter("#")


def resoudre_2(donnees):
    ancien, nouveau = None, Plan(donnees)

    while nouveau != ancien:
        ancien = nouveau.clone()

        for x in range(ancien.largeur):
            for y in range(ancien.hauteur):
                if ancien[x][y] != ".":
                    nb_places_occupees = ancien.nb_occupees_2(x, y)  # ICI ET
                    if nb_places_occupees == 0:
                        nouveau[x][y] = "#"
                    elif nb_places_occupees >= 5:  # ICI SONT DIFFERENTS.
                        nouveau[x][y] = "L"

    return nouveau.compter("#")


def main():
    donnees = lire("test")
    donnees = lire("input")
    print(resoudre_1(donnees))
    print(resoudre_2(donnees))


main()

