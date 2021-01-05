#!/usr/bin/python3


def lire(nom_fichier):
    return [int(ligne.strip()) for ligne in open(nom_fichier)]


def resoudre_1(liste, preambule):
    def valider(derniers, prochain):
        for i in derniers:
            complement = prochain - i
            if prochain != complement and complement in derniers:
                return True
        return False

    derniers = liste[:preambule]
    liste = liste[preambule:]
    while liste:
        prochain = liste.pop(0)
        if not valider(derniers, prochain):
            return prochain
        derniers.pop(0)
        derniers.append(prochain)


def resoudre_2(liste, preambule):
    mystere = resoudre_1(liste, preambule)

    sommes = []
    for i, n in enumerate(liste):
        for j in range(len(sommes)):
            sommes[j] += n
        sommes.append(n)
        if mystere in sommes:
            x = sommes.index(mystere)
            termes = liste[x:i+1]
            return min(termes) + max(termes)


def main():
    liste, preambule = lire("test"), 5
    liste, preambule = lire("input"), 25
    print(resoudre_1(liste, preambule))
    print(resoudre_2(liste, preambule))


main()

