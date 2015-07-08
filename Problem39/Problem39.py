#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme ___        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #


# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?


import time
import math


def is_solution(a,p):
    """ int * int -> bool : 
        test if the right angle triangle with right side side a and perimeter
        p has b (left side) to make a triangle """
    # given a, p and a right angle, we deduce b = frac{a^2 + 2(p-a)}{(p-a)^2}
    num = (p-a)**2 - a**2
    den = 2*(p-a)
    return (num % den) == 0

def count_sol(p):
    """ int -> int : given a permiter, we deduce the number of solutions """
    res = 0  # number of solution so far
    limit = int(math.ceil(p / (2 + math.sqrt(2) )))
    # p / (2 + math.sqrt(2) ) : we stop here, not to count solutions twice
    for a in xrange(1, limit + 1):
        if is_solution(a, p): 
            res +=1
    return res


def euler_39():
    """ unit -> int : return the solution of p39 """
    p_max = 0  # store the permiter which yields to max solutions
    max_sol = 3
    for p in xrange(2, 1000):
        number_sol = count_sol(p)
        print number_sol
        if max_sol < number_sol:
            p_max = p
            max_sol = number_sol
    return p_max

def main():
    t = time.time()
    print is_solution(30, 120)  # True
    print count_sol(120)  # 3
    print euler_39()
    print time.time() - t


# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
