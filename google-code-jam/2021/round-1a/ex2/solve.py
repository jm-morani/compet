#!/usr/bin/python3


def resoudre(L):
    nb_append = 0
    précédent = L.pop(0)
    for n in L:
        if n <= précédent:
            s_précédent, s_n = str(précédent), str(n)
            if s_précédent.startswith(s_n):
                s_x = s_précédent[len(s_n):]
                if s_x.strip("9") == "":
                    s_n += "0" * (len(s_x) + 1)
                    nb_append += len(s_x) + 1
                else:
                    x = int(s_x)
                    s_n += str(x+1).zfill(len(s_x))
                    nb_append += len(s_x)
                n = int(s_n)
            else:
                while n <= précédent:
                    n *= 10
                    nb_append += 1
        précédent = n
    return nb_append


def main():
    T = int(input().strip())
    for i in range(1, T + 1):
        N = int(input().strip())
        L = [int(x) for x in input().split(' ')]
        assert len(L) == N
        solution = resoudre(L)
        print(f"Case #{i}: {solution}")


if __name__ == "__main__":
    main()
