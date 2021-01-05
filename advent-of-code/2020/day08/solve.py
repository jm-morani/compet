#!/usr/bin/python3


def lire(nom_fichier):
    instructions = []
    for ligne in open(nom_fichier):
        operation, operande = ligne.strip().split(" ")
        instructions.append((operation, int(operande)))
    return instructions


def resoudre_1(instructions):
    ip = 0
    acc = 0
    dejavu = set({})
    while ip not in dejavu:
        operation, operande = instructions[ip]
        dejavu.add(ip)
        ip += 1
        if operation == "nop":
            continue
        if operation == "acc":
            acc += operande
            continue
        if operation == "jmp":
            ip += operande - 1
            continue
    return acc


class Infini(Exception):
    pass


def run(instructions):
    ip = 0
    acc = 0
    dejavu = set({})
    while ip not in dejavu:
        if ip == len(instructions):
            return acc
        operation, operande = instructions[ip]
        dejavu.add(ip)
        ip += 1
        if operation == "nop":
            continue
        if operation == "acc":
            acc += operande
            continue
        if operation == "jmp":
            ip += operande - 1
            continue
    raise Infini


def resoudre_2(instructions):
    for i in range(len(instructions)):
        operation, operande = instructions[i]
        try:
            if operation == "acc":
                continue
            if operation == "jmp":
                clone = instructions[:]
                clone[i] = ("nop", operande)
                return run(clone)
            if operation == "nop":
                clone = instructions[:]
                clone[i] = ("jmp", operande)
                return run(clone)
        except Infini:
            continue


def main():
    jeu = lire("test")
    jeu = lire("input")
    print(resoudre_1(jeu))
    print(resoudre_2(jeu))


main()

