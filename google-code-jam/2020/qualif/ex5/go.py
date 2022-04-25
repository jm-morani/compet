def genere_distributions(N, K):
    minimum = max(N - (N * N - K), 1)
    maximum = min(K - N + 1, N)
    print N, K, minimum, maximum

    # Distribution initiale, on charge au debut
    reste = K - N * minimum
    distribution = [minimum] * N
    for i in xrange(N):
        extra = min(reste, maximum - minimum)
        reste -= extra
        distribution[i] += extra

    yield distribution

    # Etalement progressif
    for i in xrange()
    #K2 = K - N
    #distribution = [1]
    #pass

K = 21
N = 5
distributions = genere_distributions(N, K)
for distribution in distributions:
    print repr(distribution)

