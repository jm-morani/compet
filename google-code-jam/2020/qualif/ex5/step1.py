def genere_distributions(N, K):
    minimum = max(N - (N * N - K), 1)
    maximum = min(K - N + 1, N)
    print N, K, minimum, maximum
    yield None
    
    #K2 = K - N
    #distribution = [1]
    #pass


distributions = genere_distributions(5, 5).next()
distributions = genere_distributions(5, 6).next()
distributions = genere_distributions(5, 7).next()
distributions = genere_distributions(5, 8).next()
distributions = genere_distributions(5, 9).next()
distributions = genere_distributions(5, 21).next()
distributions = genere_distributions(5, 22).next()
distributions = genere_distributions(5, 23).next()
distributions = genere_distributions(5, 24).next()
distributions = genere_distributions(5, 25).next()

#K = 9
#N = 5
#distributions = genere_distributions(K, N)
#for distribution in distributions:
#    print repr(distribution)

