#!/usr/bin/python3
import re
from sys import stdin
from collections import OrderedDict, namedtuple


Jeu = namedtuple("Jeu", ["piles", "instructions"])
Instruction = namedtuple("Déplacemement", ["quantité", "depuis", "vers"])
ESPACE = re.compile(' +')


def lire():
    tampon = []
    for ligne in stdin:
        ligne = ligne.strip('\r\n')
        if not ligne:
            break
        tampon.append(ligne)

    labels = ESPACE.split(tampon.pop().strip())
    piles = { label: [] for label in labels }
    for ligne in reversed(tampon):
        for i, label in enumerate(labels):
            caractère = ligne[i*4+1] if len(ligne) >= i*4+1 else ' '
            if caractère != " ":
                piles[label].append(caractère)

    instructions = [] 
    for ligne in stdin:
        tokens = ligne.strip("\r\n").split(" ")
        quantité = int(tokens[1])
        depuis, vers = tokens[3], tokens[5]
        instructions.append(Instruction(quantité, depuis, vers))
    return Jeu(piles, instructions)


def resoudre_1(jeu):
    piles = { label: list(pile) for label, pile in jeu.piles.items() }
    for instruction in jeu.instructions:
        for i in range(instruction.quantité):
            cageot = piles[instruction.depuis].pop()
            piles[instruction.vers].append(cageot)
    return ''.join([pile[-1] for pile in piles.values()])


def resoudre_2(jeu):
    piles = { label: list(pile) for label, pile in jeu.piles.items() }
    for instruction in jeu.instructions:
        cageots = piles[instruction.depuis][-instruction.quantité:]
        del piles[instruction.depuis][-instruction.quantité:]
        piles[instruction.vers].extend(cageots)
    return ''.join([pile[-1] for pile in piles.values()])


def main():
    jeu = lire()
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

