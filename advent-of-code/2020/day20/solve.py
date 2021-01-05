#!/usr/bin/python3

import re
from math import sqrt


TILE_REGEX = re.compile("Tile (\d+):")
MONSTRE = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


def interval(debut, borne):
    if debut < borne:
        return range(debut, borne)
    else:
        return range(debut-1, borne-1, -1)


def transformer(lignes, sens, orientation):
    n = len(lignes)
    if sens:
        lignes = [ligne[::-1] for ligne in lignes]

    for i in range(orientation):
        lignes = [
            "".join([lignes[i][n-j-1] for i in range(n)])
            for j in range(n)
        ]
    return lignes


class Piece:
    def __init__(self, numero, lignes):
        self.dejaPose = False
        self.numero = numero
        self.lignes = lignes
        self.sens = None
        self.orientation = None

        l = len(lignes)
        self.bords = {
            False: [  # Sens original
                "".join([lignes[ 0][i] for i in interval(0, l)]),  # Haut: G -> D
                "".join([lignes[i][-1] for i in interval(0, l)]),  # Droite: H -> B
                "".join([lignes[-1][i] for i in interval(l, 0)]),  # Bas: D -> G
                "".join([lignes[ i][0] for i in interval(l, 0)]),  # Gauche: B -> H
            ],
            True: [  # Pièce retournée (Gauche <=> Droite)
                "".join([lignes[ 0][i] for i in interval(l, 0)]),  # Haut: D -> G
                "".join([lignes[ i][0] for i in interval(0, l)]),  # Gauche: H -> B
                "".join([lignes[-1][i] for i in interval(0, l)]),  # Bas: G -> D
                "".join([lignes[i][-1] for i in interval(l, 0)]),  # Droite: B -> H
            ]
        }

    def orienter(self, sens, orientation):
        self.sens = sens
        self.orientation = orientation
        self.haut = self.bords[sens][(orientation + 0) % 4]
        self.droite = self.bords[sens][(orientation + 1) % 4]
        self.bas = self.bords[sens][(orientation + 2) % 4][::-1]
        self.gauche = self.bords[sens][(orientation + 3) % 4][::-1]

    def apres_rognage(self):
        l = len(self.lignes)
        lignes = transformer(self.lignes, self.sens, self.orientation)
        return [lignes[i][1:-1] for i in range(1, l-1)]


def lire(nom_fichier):
    pieces = set()
    morceaux = open(nom_fichier).read().strip().split("\n\n")
    for morceau in morceaux:
        lignes = [l.strip() for l in morceau.split("\n")]
        num = int(TILE_REGEX.match(lignes.pop(0)).group(1))
        pieces.add(Piece(num, lignes))
    return pieces


def poser(puzzle, reste, position):
    if len(reste) == 0:
        return puzzle

    (ligne, colonne) = divmod(position, len(puzzle))
    for piece in frozenset(reste):
        for sens in (False, True):
            for orientation in range(4):
                piece.orienter(sens, orientation)
                if ligne > 0 and puzzle[ligne-1][colonne].bas != piece.haut:
                    continue
                if colonne > 0 and puzzle[ligne][colonne-1].droite != piece.gauche:
                    continue

                reste.remove(piece)
                puzzle[ligne][colonne] = piece
                solution = poser(puzzle, reste, position+1)
                if solution:
                    return solution
                reste.add(piece)
    return None


def baliser(image, motif, ligne, colonne):
    hauteur = len(motif)
    largeur = len(motif[0])
    for l in range(hauteur):
        for c in range(largeur):
            if motif[l][c] == " ":
                continue
            if image[ligne+l][colonne+c] not in "#O":
                return False
    for l in range(hauteur):
        for c in range(largeur):
            if motif[l][c] == " ":
                continue
            image[ligne+l][colonne+c] = "O"
    return True


def resoudre(pieces):
    n = int(sqrt(len(pieces)))
    puzzle = [[None] * n for i in range(n)]
    poser(puzzle, pieces, 0)
    print(
        puzzle[0][0].numero * \
        puzzle[0][-1].numero * \
        puzzle[-1][0].numero * \
        puzzle[-1][-1].numero
    )

    image = []
    for ligne in puzzle:
        pieces = [piece.apres_rognage() for piece in ligne]
        for i in range(len(pieces[0])):
            image.append("")
            for piece in pieces:
                image[-1] += piece[i]

    hauteur = len(MONSTRE)
    largeur = len(MONSTRE[0])
    for sens in (False, True):
        for orientation in range(4):
            presence_monstre = False
            im = [list(ligne) for ligne in transformer(image, sens, orientation)]
            for ligne in range(0, len(im)-hauteur):
                for colonne in range(0, len(im)-largeur):
                    presence_monstre |= baliser(im, MONSTRE, ligne, colonne)

            if presence_monstre:
                # print("\n".join(["".join(ligne) for ligne in im]))
                print(sum(["".join(ligne).count("#") for ligne in im]))


def test():
    p = Piece(2311, [l.strip() for l in """
        1........2
        ..........
        ..........
        ..........
        ..........
        ..........
        ..........
        ..........
        ..........
        4........3
    """.strip().split("\n")])

    p.orienter(False, 0)
    assert p.haut   == "1........2"
    assert p.droite == "2........3"
    assert p.bas    == "4........3"
    assert p.gauche == "1........4"

    p.orienter(False, 1)
    assert p.haut   == "2........3"
    assert p.droite == "3........4"
    assert p.bas    == "1........4"
    assert p.gauche == "2........1"

    p.orienter(False, 2)
    assert p.haut   == "3........4"
    assert p.droite == "4........1"
    assert p.bas    == "2........1"
    assert p.gauche == "3........2"

    p.orienter(False, 3)
    assert p.haut   == "4........1"
    assert p.droite == "1........2"
    assert p.bas    == "3........2"
    assert p.gauche == "4........3"

    p.orienter(True, 0)
    assert p.haut   == "2........1"
    assert p.droite == "1........4"
    assert p.bas    == "3........4"
    assert p.gauche == "2........3"

    p.orienter(True, 1)
    assert p.haut   == "1........4"
    assert p.droite == "4........3"
    assert p.bas    == "2........3"
    assert p.gauche == "1........2"

    p.orienter(True, 2)
    assert p.haut   == "4........3"
    assert p.droite == "3........2"
    assert p.bas    == "1........2"
    assert p.gauche == "4........1"

    p.orienter(True, 3)
    assert p.haut   == "3........2"
    assert p.droite == "2........1"
    assert p.bas    == "4........1"
    assert p.gauche == "3........4"

    """
    print("\n".join(p.lignes))
    print("\n".join(transformer(p.lignes, True, 0)))
    print("\n".join(transformer(p.lignes, False, 1)))
    print("\n".join(transformer(p.lignes, True, 1)))
    """


def main():
    test()
    pieces = lire("test")
    pieces = lire("input")
    resoudre(pieces)


main()

