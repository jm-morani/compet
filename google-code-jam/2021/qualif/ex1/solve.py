#!/usr/bin/python3


def resoudre(N, L):
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


def main():
    T = int(input().strip())
    for i in range(1, T + 1):
        N = int(input().strip())
        L = [int(x) for x in input().split(' ')]
        assert len(L) == N
        solution = resoudre(N, L)
        print(f"Case #{i}: {solution}")


main()

