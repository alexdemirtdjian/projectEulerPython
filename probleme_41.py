#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 41        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
# also prime.

# What is the largest n-digit pandigital prime that exists?


import time
import primes as pm


s = pm.Sieve(10**7)
lst_primes = s.listPrimes()  # list of primes under 10**9

def check_pandigital(n):
    """ int -> bool : check if n is a pandigital number"""
    length = len(str(n))
    return set(range(1, length+1)) == set(map(int, list(str(n))))


def euler_41():
    """ unit -> int : find the largest n-pandigital prime """
    # we start from the end of the list (the largest primes)
    # so the first we find if the largest.
    for i in reversed(lst_primes):
        if check_pandigital(i):
            return i

def main():
    t = time.time()
    print check_pandigital(2143)
    print euler_41()
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
