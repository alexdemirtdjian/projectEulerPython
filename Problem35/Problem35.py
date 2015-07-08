#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : problem 35        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.

# How many circular primes are there below one million?


import time
import primes as p


crible = p.Sieve(1000000)  # a sieve for getting primes below 10**6
first_primes = crible.listPrimes()


def rotate(n):
    """ int -> int list : return a list containg circular rotation of n"""
    rotlist = []
    m = str(n)
    counter = 0
    while counter < len(str(n)):
        m = m[1:] + m[0]  # rotation one time : one step left
        rotlist.append(int(m))
        counter += 1
    return rotlist

def is_circular(n):
    """ int -> bool : test if n is a circular prime """
    l = rotate(n)  # liste containing all rotations of n
    g = lambda m: crible.isPrime(m)
    return all(map(g,l)) 

def euler_35():
    res = 0  # number of circular primes below 10**6
    for i in range(len(first_primes)):
        if is_circular(first_primes[i]):
            res +=1
    return res

def main():
    # print first_primes[-1]  # 999983
    # print is_circular(197)  # True
    t = time.time()
    print euler_35()
    print time.time() - t



# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
