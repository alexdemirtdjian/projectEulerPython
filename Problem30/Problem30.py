#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 30        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# Surprisingly there are only three numbers that can be written as the sum of 
# fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth 
# powers of their digits.

import time

# we notice that the for loop will end at 5 digit number since
# 6*9**5 = 354294 < 10**6

def explode(n):
    """ int -> int list : explode into a list"""
    if n<10:
        return [n]
    else:
        (a,b) = (n%10, n/10)
        return explode(b) + [a]

def is_power_five(n):
    """ int -> bool : test if n can be written as the sum of fifth powers"""
    l = explode(n)
    g = lambda x: x**5
    return sum(map(g, l)) == n


def euler_30():
    """ unit -> int """
    res = 0
    for i in xrange(2,10**6):
        if is_power_five(i):
            res += i
    return res

def main():
    t = time.time()
    # print explode(234567)
    print euler_30()
    print time.time() - t
    
# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
