def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    primes = [2]

    for p in range(3, n + 1, 2):
        if is_prime[p]:
            primes.append(p)

            for multiple in range(p * p, n + 1, p + p):
                is_prime[multiple] = False

    return primes


def PrimePi(n):
	PrimeList = sieve_of_eratosthenes(n)
	return len(PrimeList)


primesLessThanEqn = sieve_of_eratosthenes(50)

for i in primesLessThanEqn:
	print(i,end=' ')

pi_x = PrimePi(100)
print('\n', pi_x) 