import numpy as np


def euler6():
    question = "Find the difference between the sum of the squares of the " \
               "first one hundred natural numbers and the square of the sum."
    # recall sum(1..n) = n(n+1)/2
    square_sum = np.power(100*101/2, 2)
    sum_square = 0
    for i in range(100):
        sum_square += (i*i)
    return question, int(square_sum-sum_square)


def euler7():
    question = "What is the 10,001st prime number?"
    # https://www.quora.com/What-is-the-code-for-applying-sieve-of-eratosthenes-in-C-programming
    def sieve(n):
        # return an array  where
        # prime[i] = False means number i is not prime
        # prime[i] = True  means number i is prime
        primes = np.ones((n, 1))
        primes[0] = primes[1] = False
        for i in range(2, int(np.ceil(np.sqrt(n)))):
            for j in range(i*i, n, i):
                primes[j] = False
        return primes

    primes = sieve(200000)
    prime_counter = 0
    enter_break = False
    i = -1
    for i, is_prime in enumerate(primes):
        if is_prime:
            prime_counter += 1
            if prime_counter >= 10001:
                enter_break = True
                break
    if enter_break:
        return question, i
    else:
        print("Choose larger init for sieve")


def euler8():
    return None, None


def euler9():
    question = "There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc."
    for a in range(0, 1000):
        for b in range(0, a):
            c = np.sqrt(a*a + b*b)
            if a+b+c == 1000:
                return question, int(a*b*c)
    print("Error")


def euler10():
    question = "Find the sum of all the primes below two million."
    # https://www.quora.com/What-is-the-code-for-applying-sieve-of-eratosthenes-in-C-programming
    def sieve(n):
        # return an array  where
        # prime[i] = False means number i is not prime
        # prime[i] = True  means number i is prime
        primes = np.ones((n, 1))
        primes[0] = primes[1] = False
        for i in range(2, int(np.ceil(np.sqrt(n)))):
            for j in range(i*i, n, i):
                primes[j] = False
        return primes

    primes = sieve(2000000)
    total = 0
    for i, is_prime in enumerate(primes):
        if is_prime:
            total += i
    return question, total


