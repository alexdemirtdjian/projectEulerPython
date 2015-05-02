#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme ___        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #


# It was proposed by Christian Goldbach that every odd composite number can be 
# written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a 
# prime and twice a square?

import primes as pr
import time


crible = pr.Sieve(10**4)
prime_lst = crible.listPrimes()  # list of primes


def is_sqrt(n):
    """ int -> bool : is n a squared number """
    x = n
    y = (x + 1) / 2
    while y < x:
        x = y
        y = (x + n / x) / 2
    return x*x == n

def is_solution(n):
    """ int -> bool : try to find if n can be written as prime + 2*square """
    i = 0
    while prime_lst[i] < n:
        if is_sqrt((n - prime_lst[i]) / 2):
            return True
        else:
            i+= 1
    return False  # we didn't find a poper prime to fit

def euler_46():
    """ unit -> int : find the first add composite not solition """
    i = 1
    found = False  # have we found it ?
    while not(found):
        if not((2*i + 1) in prime_lst) and not(is_solution((2*i + 1))):
            # it is an odd composite number
            found = True
        i += 1
    return (2*i - 1)


def main():
    print is_sqrt(42)  # False
    print is_sqrt(25)  # True
    t = time.time()
    print euler_46()
    print time.time() - t


# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
