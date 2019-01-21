import numpy as np


def euler1():
    question = "Find the sum of all the multiples of 3 or 5 below 1000."
    total = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return question, total


def euler2():
    question = "By considering the terms in the Fibonacci sequence whose values do not exceed four million, " \
               "find the sum of the even-valued terms."
    total = 0
    fib_num = 1
    fib_num_prev = 1
    while fib_num_prev < 4000000:
        if fib_num % 2 == 0:
            total += fib_num
        fib_num, fib_num_prev = fib_num+fib_num_prev, fib_num
    return question, total


def euler3():
    question = "What is the largest prime factor of the number 600851475143."
    num = 600851475143
    # num is an odd number so do not have to worry about 2
    # iterate through odd numbers (because only odd primes left)
    # as iterate from smallest to largest odd numbers, when divisible, i will be a prime number
    # divide out "i"
    i = 1
    while num > i:  # stop when num greater because cannot divide out anymore
        i += 2  # add 2 because prime numbers will be odd
        while num % i == 0:  # divide out all powers of the prime number
            num /= i
    return question, i


def euler4():
    question = "Find the largest palindrome made from the product of two 3-digit numbers."
    current_max = 0
    for i in range(100, 999):
        for j in range(100, i):
            product = i*j
            product_str = str(product)
            if product_str == product_str[::-1] and product > current_max:
                current_max = product
    return question, current_max


def euler5():
    question = "What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"
    # easy to do manually
    # break up the numbers from 1 to 20 into their prime factorization
    # 1, 2, 3, 2^2, 5, 2*3, 7, 2^3, 3^2, 2*5, 11, (2^2)*3, 13, 2*7, 3*5, 2^4, 17, 2*(3^2), 19, (2^2)*5
    # for each prime number, find the number where the prime number is used most often
    # 2,  : 16   ->   2^4
    # 3,  : 9/18 ->   3^2
    # 5,  : 5    ->   5^1
    # 7,  : 7    ->   7^1
    # 11, : 11   ->  11^1
    # 13, : 13   ->  13^1
    # 17, : 17   ->  17^1
    # 19, : 19   ->  19^1
    # So the solutions is the product of the last column
    # 2^4 * 3^2 * 5^1 * 7^1 * 11^1 * 13^1 * 17^1 * 19^1
    answer = np.power(2, 4) * np.power(3, 2) * 5 * 7 * 11 * 13 * 17 * 19
    return question, answer
