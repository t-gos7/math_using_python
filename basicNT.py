#NumberTh functions with SymPy package 
#-------------------------------------

from sympy import ntheory
from sympy import sieve
from sympy import generate

sieve._reset() # An infinite list of prime numbers, implemented as a dynamically growing sieve of Eratosthenes.#When a lookup is
# requested involving an odd number that has not been sieved,the sieve is automatically extended up to that number.

print(13 in sieve)  # prints 'True' if the input is prime,

sieve.extend(40) #for input n grows the sieve to contain all primes <= n 

print(sieve[10])  # returns n th prime

sieve.extend_to_no(15)  # extends upto n th prime


# mobiusrange(a,b) genarates Mobius numbers for the range [a,b), means output will be a list.
Mob_func = sieve.mobiusrange(7,12)
print('\n Mobius function outputs in the given range:',[i for i in Mob_func])


# primerange(a,b) generates all prime numbers in the range [a,b)
Prime_list = sieve.primerange(1,5)
print('\n Primes in the given range are :',[i for i in Prime_list])


#search(n) return the indices i, j of the primes that bound n. If n is prime then i == j. Although n can be an expression,
# if ceiling cannot convert it to an integer then an error will be raised.
x,y = sieve.search(25)
print('\n The given input is in between ','(',x,',',y,')','th Primes \n')


#totientrange(a, b) generates all totient numbers for the range [a, b). Simply it is a list of outputs
Totient_range = sieve.totientrange(1,10)
print(' Values of Totient(n):' ,[i for i in Totient_range])


#sympy.ntheory.generate.prime(nth)  return the n th prime number. Logarithmic integral of x is a pretty nice approximation
# for number of primes <= x, i.e. li(x) ~ pi(x) 
print('\n','See this! The 1000000th prime: ', generate.prime(1000000))


#sympy.ntheory.generate.primepi(n) returns the value of the prime counting function pi(n) = the number of prime numbers
# less than or equal to n.
print('\n','There are ',generate.primepi(40),' primes < or = the given input')


#sympy.ntheory.generate.nextprime(n, ith=1) return the ith prime greater than n
print('\n','Next 5th prime after 2 is ',generate.nextprime(2, ith=5))


#sympy.ntheory.generate.prevprime(n) return the largest prime smaller than n
print('\n','Largest previous prime of given input: ', generate.prevprime(8))
















