#!/usr/bin/python3

from collections import defaultdict

MX = 12 * 60 * 60 * 1000000000


def normaliser(a, b, c):
    def angle(x, y):
        xy = (x - y + MX) % MX
        return xy if xy < MX // 2 else MX - xy
    ab = angle(a, b)
    bc = angle(b, c)
    ca = angle(c, a)
    #angles = [ab, bc, ca]
    #return tuple(sorted(angles))
    if ca > ab and ca > bc:
        return (ca, ab, bc)
    if ab > ca and ab > bc:
        return (ab, bc, ca)
    return (bc, ca, ab)


def precalculer():
    precalcul = defaultdict(list)
    a = 0
    for h in range(12):
        b = 0
        for m in range(60):
            c = 0
            for s in range(60):
                clef = normaliser(a, b, c)
                if (h,m,s) == (6,30,0):
                    print(630, (a,b,c), clef)
                #if clef in precalcul:
                #    print((a,b,c), (h,m,s) , precalcul[clef])
                precalcul[clef].append((h, m, s))
                a += 1 * 1000000000
                b += 12 * 1000000000
                c += 720 * 1000000000
    #for (clef, (h,m,s)) in precalcul.items():
    #    if (h,m,s) == (6, 30, 0):
    #        print('630', clef)
    return precalcul


def resoudre(precalcul, A, B, C):
    print(A, B, C)
    clef = normaliser(A, B, C)
    print(precalcul[clef])
    #h, m, s = precalcul[clef]
    #return (h, m, s, 0)
    return 0, 0, 0, 0


def main():
    precalcul = precalculer()
    T = int(input().strip())
    for x in range(1, T + 1):
        (A, B, C) = [int(i) for i in input().split(' ')]
        (h, m, s, n) = resoudre(precalcul, A, B, C)
        print(f"Case #{x}: {h} {m} {s} {n}")


if __name__ == "__main__":
    main()
