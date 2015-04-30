#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme ___        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# Euler discovered the remarkable quadratic formula:
#
# n² + n + 41
# 
# It turns out that the formula will produce 40 primes for the consecutive 
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is 
# divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly 
# divisible by 41.

# The incredible formula  n² − 79n + 1601 was discovered, which produces 80 
# primes for the consecutive values n = 0 to 79. The product of the 
# coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n² + an + b, where |a| < 1000 and |b| < 1000

# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.

import time
import primes


crible = primes.Sieve(100000)
l = crible.listPrimes()
first_primes = l[:2000]  # we extract the 200 first primes  

def f(a,b):
    """ int*int -> int->int """
    g = lambda n: (n**2 + a*n + b)
    return g

def find(a, l):
    """ int * int list -> bool : find if a is in l assuming l sorted """
    i = 0
    while (l[i] != a) and (l[i] < a):
        i+=1
    return l[i] == a  

def euler_27():
    """ unit -> int : solution of problem """
    cur_max_primes = 40  # accordiing to the subject we can reach 40
    res_couple = (0,0)
    for a in range(-999,1000):
        for b in range(-999,1000):
            n_cur = 0  # the current n, we will match f(a,b)(n) with l[n]
            while find(f(a, b)(n_cur), l):
                n_cur += 1
            if n_cur > cur_max_primes:
                res_couple = (a,b)
                cur_max_primes = n_cur
    return res_couple, cur_max_primes




def main():
    # print first_primes
    # print find(f(1, 41)(3), l)
    t = time.time()
    print euler_27()
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
