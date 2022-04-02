#!/usr/bin/python3

import sys
sys.setrecursionlimit(10000000)


class Noeud:
    def __init__(self, fun):
        self.fun = fun
        self.suivant = None
        self.ancêtres = []
        self.ennuyant = None

    def inventorier(self, inventaire):
        inventaire.remove(self)
        for ancêtre in self.ancêtres:
            ancêtre.inventorier(inventaire)

    def retro_propager(self):
        if len(self.ancêtres) == 0:
            return self.fun

        ancêtre = self.ancêtres[0]
        fun = ancêtre.retro_propager()
        min_fun, pire = fun, ancêtre

        for ancêtre in self.ancêtres[1:]:
            fun = ancêtre.retro_propager()
            if fun < min_fun:
                min_fun, pire = fun, ancêtre

        self.ennuyant = pire
        return max(self.fun, min_fun)

    def calculer(self):
        if len(self.ancêtres) == 0:
            return 0, self.fun

        m = 0
        total = 0
        for ancêtre in self.ancêtres:
            if ancêtre == self.ennuyant:
                tot, fun = ancêtre.calculer()
                total += tot
                m = max(self.fun, fun)
            else:
                tot, fun = ancêtre.calculer()
                total += tot + fun
        return total, m


def resoudre(F, P):
    noeuds = [Noeud(f) for f in F]

    # On pointe les suivants et les ancêtres.
    racines = []
    for noeud, p in zip(noeuds, P):
        if p:
            suivant = noeuds[p-1]
            noeud.suivant = suivant
            suivant.ancêtres.append(noeud)
        else:
            racines.append(noeud)

    # On remplace les cycles.
    inventaire = set(noeuds)
    for racine in racines:
        racine.inventorier(inventaire)
    while inventaire:
        # Trouve le départ d'un cycle
        départ = next(iter(inventaire))
        déjà_vus = set()
        while True:
            déjà_vus.add(départ)
            départ = départ.suivant
            if départ in déjà_vus:
                break
        # Aggrège le cycle
        suivant = départ
        max_fun, ancêtres = 0, set()
        supprimés = set()
        while True:
            suivant = suivant.suivant
            max_fun = max(max_fun, suivant.fun)
            ancêtres |= set(suivant.ancêtres)
            supprimés.add(suivant)
            if suivant == départ:
                break
        # Insère l'aggrégat
        racine = Noeud(max_fun)
        racine.ancêtres = list(ancêtres - supprimés)
        racines.append(racine)
        inventaire -= supprimés
        inventaire.add(racine)
        racine.inventorier(inventaire)

    # Calcul du résultat
    for racine in racines:
        racine.retro_propager()
    return sum(sum(racine.calculer()) for racine in racines)


def main():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        F = [int(f) for f in input().split(' ')]
        assert len(F) == N
        P = [int(p) for p in input().split(' ')]
        assert len(P) == N
        solution = resoudre(F, P)
        print(f"Case #{i}: {solution}")


main()
