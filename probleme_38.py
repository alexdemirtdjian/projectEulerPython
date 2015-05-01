#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 38        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #


# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
# call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 
# and 5, giving the pandigital, 918273645, which is the concatenated product 
# of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
# concatenated product of an integer with (1,2, ... , n) where n > 1?


# we will check the number of type 
# 'ab' x [1,2,3,4] 
# 'abc' x [1,2,3] 
# 'abcd' x [1,2]
# all others are overflowing on 10 digits

import time


def check_pandigital(n, l):
    """ int * int list -> bool * int : 
        check if n is a matching number, also return the product concatenated"""
    s = "0"
    for i in l:
        s += str(i*n)
    # we check if we have 10 digits and no duplicates
    return ((len(s) == 10) and (len(list(set(s))) == 10), int(s[1:])) 

def euler_38():
    """ unit -> int : find the largest pandigital numer of the problem """
    cur_res = 0  # We put here the largest number found so for
    # Check of 'ab' x [1,2,3,4] 
    l1 = range(1,5)
    for i in xrange(10,100):
        if check_pandigital(i, l1)[0]:
            if check_pandigital(i, l1)[1] > cur_res:
                cur_res = check_pandigital(i, l1)[1]
    # Check of 'abc' x [1,2,3] 
    l2 = range(1,4)
    for i in xrange(100,1000):
        if check_pandigital(i, l2)[0]:
            if check_pandigital(i, l2)[1] > cur_res:
                cur_res = check_pandigital(i, l2)[1]
    # Check of 'abcd' x [1,2]
    l3 = range(1,3)
    for i in xrange(1000,10000):
        if check_pandigital(i, l3)[0]:
            if check_pandigital(i, l3)[1] > cur_res:
                cur_res = check_pandigital(i, l3)[1]
    return cur_res


def main():
    print check_pandigital(192, range(1,4))  # True
    t = time.time()
    print euler_38()
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
