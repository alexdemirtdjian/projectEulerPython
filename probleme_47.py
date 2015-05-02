#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme ___        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors. 
# What is the first of these numbers?

import primes as pr
import time


crible = pr.Sieve(10**6)
lst = crible.listPrimes()  # we list the first primes

def factorise_rec(n, l):
    """ int * int list -> int list : factorise to prime """
    if crible.isPrime(n):
        return l + [n]
    else:
        i = 0
        while (n % lst[i] != 0):
            i+= 1
        n2, l2 = (n/lst[i]), l + [lst[i]]
        return factorise_rec(n2, l2)


def number_of_factor(n):
    """ int -> int : return the number of distinct prime factors """
    return len(set(factorise_rec(n, [])))


def euler_47():
    """ unit -> int : find the solution """
    for i in xrange(2, 10**6):
        if [number_of_factor(j) for j in range(i, i+4)] == [4]*4:
            return i



def main():
    t = time.time()
    # print factorise_rec(342, [])  # [2, 3, 3, 19]
    # print number_of_factor(3)
    print euler_47()
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
