#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme ___        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
# by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) 
# each of the 4-digit numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this 
# sequence?

import time
import primes

# we generate the 4 digits prime numbers
pr_lst = primes.Sieve(10**4).listPrimes()


# we notice there is two parameters :
# * the gap of the arithemtic sequence
#   the gap is roughtly between [1 - 4500] since all primes are 4-digits
#   1000 + 2*gap < 10**5
# * the first prime number
#   which starts from 1009 up to 9973

def explode(n):
    """ 
    int -> int list
    """
    if n < 10:
        return [n]
    else:
        (a, b) = (n % 10, n / 10)
        return explode(b) + [a]

def euler_49():
    """ 
    unit -> int : find the solution of euler 49
    """
    for p in pr_lst:
        # we first get rid of 3 digits primes
        if p < 1500:
            continue
        else:
            for gap in xrange(1, 4500):
                if (p + gap) in pr_lst and (p + 2*gap) in pr_lst:
                    if set(explode(p)) == set(explode(p + gap)) and set(explode(p)) == set(explode(p + 2*gap)): 
                        return p, p+gap, p+2*gap




def main():
    # print pr_lst
    # print explode(124)
    t = time.time()
    print euler_49()
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
