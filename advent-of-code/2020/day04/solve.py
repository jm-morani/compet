#!/usr/bin/python3

import re


CONNUES = {
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
}


def lire(nom_fichier):
    passeports = []
    passeport = {}
    for ligne in open(nom_fichier):
        ligne = ligne.strip()
        if ligne:
            for champ in ligne.split(" "):
                clef, valeur = champ.split(":")
                passeport[clef] = valeur
        else:
            passeports.append(passeport)
            passeport = {}
    passeports.append(passeport)
    return passeports


def resoudre_1(passeports):
    n = 0
    for passeport in passeports:
        clefs = set(passeport.keys())
        if clefs == CONNUES:
            n += 1
        elif CONNUES - clefs == {"cid"}:
            n += 1
    return n


HCL = re.compile("^#[0-9a-f]{6}$")
ECL = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
PID = re.compile("^[0-9]{9}$")


def valide(passeport):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    try:
        assert(1920 <= int(passeport["byr"]) <= 2002)
        assert(2010 <= int(passeport["iyr"]) <= 2020)
        assert(2020 <= int(passeport["eyr"]) <= 2030)

        unite = passeport["hgt"][-2:]
        if unite == "cm":
            assert(150 <= int(passeport["hgt"][:-2]) <= 193)
        elif unite == "in":
            assert(59 <= int(passeport["hgt"][:-2]) <= 76)
        else:
            assert(False)

        assert(HCL.match(passeport["hcl"]))
        assert(passeport["ecl"] in ECL)
        assert(PID.match(passeport["pid"]))

    except (KeyError, AssertionError):
        return False
    return True


def resoudre_2(passeports):
    n = 0
    for passeport in passeports:
        if valide(passeport):
            n += 1
    return n


def main():
    #jeu = lire("test")
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

