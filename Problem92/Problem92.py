#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 92       			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #


# A number chain is created by continuously adding the square of the digits in 
# a number to form a new number until it has been seen before.

# For example,

# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
# What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

# How many starting numbers below ten million will arrive at 89?


# key value dictionary
# we remembered the number we have seen so we don't recalculate the whole chain
dict_chain = {1:False, 89:True}

def int_split(n):
    """ int -> int list : convert int to list of its digit """
    return map(lambda d: int(d), list(str(n)))

def terminate(n):
    """ int -> bool : check if terminating number of the chain is 89 """
    try:
        return dict_chain[n]
    except:
        res = terminate(sum(map(lambda k: k**2, int_split(n))))
        dict_chain[n] = res
        return res

def euler_92():
    """ unit -> int """
    res = 0
    for i in xrange(1, 10**7):
        if(terminate(i)):
          res+=1
    return res


def main():
    print int_split(1223234)
    print terminate(44)  # False
    print terminate(85)  # True
    print dict_chain
    print euler_92()


# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
