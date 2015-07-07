#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 63        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

# a_1a_2...a_n = k**n
# a_1 * 10**(n-1) + a_2 * 10**(n-2) + ... + a_n = k**n

# 9**10 = a_1 * 10**9 
# 9**10 = 3486784401
# 9**11 = 31381059609 ...

# [(i, len(str(i**10))) for i in xrange(30)]

# shows us that 9**21 yields 21 digits number ok
# 9**22 yields 21 digits numbers so
# if a number is 22 digits long, m = a_1..a_22 it won't
# in form m = k**22 since k**22 < 9**22 < 10**22 >= m
# then we show that adding a digits won't be caught up by multiplying by a digits k**n

# we scan the range of number from 1 to 10**21

import time

def check(m, n):
    """
    int * int -> bool : check if m, an n digit number is an n-th poser
    """
    for k in range(1, 10):
        if (k**n > m):
            return False  # we overflow, we stop
        elif (k**n == m):
            return True  # got it
    return False  # we scan all digits, it's false then


def euler_63():
    """ unit -> int : return project euler 63 solution """
    res = 0
    for k in xrange(1, 10):
        for n in xrange(1, 22):
            if (len(str(k**n)) == n):
                res +=1
    return res





def main():
    # print check(134217728, len(str(134217728))) : True
    # print 134 in [_**3 for _ in range(10)] : False
    # print check(134, len(str(134))) : False
    print euler_63()




# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
