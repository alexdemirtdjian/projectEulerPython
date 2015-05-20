#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme ___        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 
# is almost unimaginably large: one followed by two-hundred zeros. Despite their 
# size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, ab, where a, b < 100, what is the 
# maximum digital sum?

import time

def sum_digits(n):
    """ int -> int list : return the list of digits """
    return sum([int(c) for c in str(n)])


def euler_56():
    """ unit -> int : find the number with greater digital sum of form a**b """
    res = 0
    for a in xrange(1, 101):
        for b in xrange(1, 101):
            s = sum_digits(a**b)
            if s > res:
                res = s
    return res


def main():
    print sum_digits(223454)  # 20
    t = time.time()
    print euler_56()
    print time.time() - t


# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
