
def verifier(suite):
    X = len(suite)
    res=set()
    for i in range(2**X):
        A, B = 0, 0
        for x in range(X):
            if i & 2 ** x == 0:
                A += suite[x]
            else:
                B += suite[x]
        print("  - ", i, max(A-B, B-A))
        res.add(max(A-B, B-A))
    return res


def obtenir(x, suite):
    l = len(suite)
    A, B = 0, 0
    U = 2**(l-1) - (x + 1)  // 2
    for x in range(l):
        if U & 2 ** x == 0:
            A += suite[x]
        else:
            B += suite[x]
    return A-B

def obtenir2(x, suite, gen):
    l = len(suite)
    A, B = 0, 0
    U = sum(suite) - x # ((l+1)*2)-1 - x
    for x in range(l):
        if U & 2 ** x == 0:
            A += suite[x]
        else:
            B += suite[x]
    return A-B

def tester(suite):
    gen = list(sorted(verifier(suite)))
    print(repr(suite) + " " + repr(gen))
    #for n in gen:
    #    x = obtenir2(n, suite, gen)
    #    print(' ', n, ' => ', x)
        

#tester([1, 2])
#tester([1, 2, 3, 4])
tester([1, 2, 3, 4, 5])
#tester([1, 2, 3, 5, 8]) # fib optimal
#tester([1, 2, 3, 5, 9]) # fib optimal
#tester([1, 2, 3, 5, 7]) # fib optimal
#tester([1, 2, 4, 8, 16]) # optimal
#tester([1, 2, 4])
#tester([1, 3, 6])

