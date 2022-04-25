#!/usr/bin/python3

import sys
sys.setrecursionlimit(1500)


def resoudre_ex1(N, L):
    positions = [0] * N            
    for pos, val in enumerate(L):
        positions[val-1] = pos

    cout = 0    
    for i in range(N-1):
        j = positions[i]
        cout += j - i + 1
        for k, pos in enumerate(positions):
            if i <= pos <= j:                
                positions[k] = j - pos + i

    return cout


def resoudre(N, C):
    def parcourir(debut, n, reste):
        if n == N:
            if resoudre_ex1(N, debut) == C:
                return debut
        else:
            for i, x in enumerate(reste):
                nvo_reste = reste[:]
                debut[n] = nvo_reste.pop(i)
                res = parcourir(debut, n+1, nvo_reste)
                if res:
                    return res

    if N-1 <= C <= N*(N+1)//2-1:
        return parcourir([0]*N, 0, list(range(1, N+1)))


def main():
    T = int(input())
    for i in range(1, T + 1):
        N, C = [int(x) for x in input().split(' ')]
        solution = resoudre(N, C)
        solution = ' '.join([str(x) for x in solution]) if solution else 'IMPOSSIBLE'
        print(f"Case #{i}: {solution}")


main()

