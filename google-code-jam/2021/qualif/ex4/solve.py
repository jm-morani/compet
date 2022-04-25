#!/usr/bin/python3

from sys import stderr

def resoudre(N):
    def lire(a, b, c):
        print(f"{a+1} {b+1} {c+1}", flush=True)
        return int(input()) - 1
    
    med = lire(0, 1, 2)
    solution = [0, 1, 2] if 0 != med else (1, med, 2)
    for range(4, N+1):
        
        
    print(, file=stderr)
    return list(range(N))


def main():
    T, N, Q = [int(x) for x in input().split(' ')]
    for i in range(1, T + 1):
        solution = resoudre(N)
        print(' '.join([f"{n+1}" for n in solution]), flush=True)
        assert(input() == '1')


main()
