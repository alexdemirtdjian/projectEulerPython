#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 39        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #


# The number 3797 has an interesting property. Being prime itself, it is possible
# to continuously remove digits from left to right, and remain prime at each 
# stage: 3797, 797, 97, and 7. Similarly we can work from right to 
# left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to 
# right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


import time
import primes


crible = primes.Sieve(10**6)
crible_list = crible.listPrimes()

def is_truncatable_prime(n):
    """ int -> bool : test if n is a truncatable prime """
    lth = len(str(n))
    # We check quikly if 
    if not(int(str(n)[0]) in [2, 3, 5, 7]):
        return False
    trunc_lst = []  # a list containing the truncation of n
    for i in xrange(1,lth):
        trunc_lst.append( int(str(n)[0:i]) )
        trunc_lst.append( int(str(n)[i:lth]) )
    g = lambda n: n in crible_list
    return all(map(g, trunc_lst))


def find_all_truncable():
    res = []
    i = 4  # thus we eliminate the 2, 3, 5 and 7
    while(len(res) != 11):  # we know they are 11
        if is_truncatable_prime(crible_list[i]):
            res.append(crible_list[i])
            print res
        print crible_list[i]
        i += 1
    return res



def main():
    print is_truncatable_prime(3797)  # True
    print find_all_truncable()


# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
