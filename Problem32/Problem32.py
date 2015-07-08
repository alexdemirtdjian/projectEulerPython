#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 32        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 
# through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
# multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity 
# can be written as a 1 through 9 pandigital.


# We try the multiplication of type a x bcde and ab x cde
# the others are either symetric are lead to too much digits

import time


def check_pandigital(n,m,p):
    """ int * int * int -> bool : check if it yields to pandigital """
    s = str(n) + str(m) + str(p) + '0'  # we concatenate all int and add 0
    # we check if we have 10 digits and no duplicates
    return (len(s) == 10) and (len(list(set(s))) == 10)   

def euler_32():
    """ unit -> int : find the sum of the problem """
    res = 0  # the sum
    found = []  # the int already found
    # first we check the products of type 'a x abcd'
    for i in xrange(1,10):
        for j in xrange(1000,10000):
            p = i*j
            if check_pandigital(i, j, p):
                if not(p in found):  # we have not already found it once
                    found.append(p)
    # we check the products of type 'ab x cde'
    for i in xrange(10,100):
        for j in xrange(100,1000):
            p = i*j
            if check_pandigital(i, j, p):
                if not(p in found):  # we have not already found it once
                    found.append(p)
    print found
    return sum(found)


def main():
    t = time.time()
    #  print check_pandigital(123,456,7890)  # True
    print euler_32() 
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
