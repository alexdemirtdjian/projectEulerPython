#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme ___        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below 
# one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, 
# contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most 
# consecutive primes?

import time
import primes


# we start by generating the primes below 10**6
lst = primes.Sieve(10**6).listPrimes()


def euler_50():
    res = 1  # the max length we will found
    size = len(lst)
    for i in xrange(size):
        print lst[i]
        for j in range(i + res, size):  
            # j will be the position of the last prime in the sum
            # as the max length we restrict the area we search
            chunk = lst[i:j+1]  # we sub list the primes we will try to add
            chunklength = len(chunk)
            chunktotal = sum(chunk)
            if chunktotal > 10**6:
                break
            if chunktotal in lst:
                if chunklength > res:  # we have found sth with greater length
                    res = chunklength  # we update the res
                    prime_res = chunktotal
    return res, prime_res



def main():
    print euler_50()

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
