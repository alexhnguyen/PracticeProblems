import numpy as np


def euler11():
    return None, None


def euler12():
    question = "What is the value of the first triangle number to have over five hundred divisors?"
    def get_num_divisiors(n):
        # https://en.wikipedia.org/wiki/Divisor_function
        # if n = (p^a)*(q^b)*(r^c) then
        # number of divisors is (a+1)*(b+1)*(c+1)
        num_divisors = 1
        while n % 2 == 0 and n != 0:
            num_divisors += 1
            n /= 2
        for i in range(3, int(n)+1, 2):
            factors = 1
            while n % i == 0 and n != 0:
                factors += 1
                n /= i
            num_divisors *= factors
            if n == 1:
                break
        return num_divisors

    triangle_number = 1
    i = 1
    while True:
        if get_num_divisiors(triangle_number) > 500:
            break
            # return
        i += 1
        triangle_number += i
    return question, triangle_number


def euler13():
    return None, None


def euler14():
    question = "Which starting number, under one million, produces the longest collatz chain?"
    def collatz(n):
        if n % 2 == 0:
            n /= 2
        else:
            n *= 3
            n += 1
        return int(n)
    numbers = 1000000
    # as collatz sequences follow similar paths, .. -> 8 -> 4 -> 2 -> 1
    # use dynamic programming concept
    collatz_counter = np.zeros((numbers*numbers, 1))
    collatz_counter[1] = 1
    largest_chain = 1
    largest_index = 1
    for i in range(2, numbers):
        i_ = i
        chain_count = 0
        while i != 1:
            if collatz_counter[i] != 0:
                collatz_counter[i_] = collatz_counter[i] + chain_count
                if collatz_counter[i_] > largest_chain:
                    largest_chain = collatz_counter[i_]
                    largest_index = i_
                break
            else:
                i = collatz(i)
                chain_count += 1
        if i == 1:
            collatz_counter[i_] = collatz_counter[i] + chain_count
    return question, largest_index


def euler15():
    question = "Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, " \
               "there are exactly 6 routes to the bottom right corner.\n " \
               "How many such routes are there through a 20×20 grid?"
    total = 1
    dim = 20
    for i in range(1, dim+1):
        total = total * (dim + i) / i
    return question, int(total)
