#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 33        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is 
# correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less 
# than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

import time


def euler_33():
    """ unit -> int*int list : find the curious fractions """
    fractions_found = []
    for i in xrange(10,99):
        for j in xrange(i+1,100):  # we have here the condition i/j < 1
        # we eliminate trivial fractions
            if (i % 10 == 0) and (j % 10 == 0): 
                continue
            (a,b) = (int(str(i)[0]), int(str(i)[1]))
            (c,d) = (int(str(j)[0]), int(str(j)[1]))
            if (a == c):
                # we test if 'i/j = ab/cd = b/d'
                if (i*d == j*b):
                    fractions_found.append((b,d))
            elif (a == d):
                if (i*c == j*b):
                    fractions_found.append((b,c))
            elif (b == c):
                if (i*d == j*a):
                    fractions_found.append((a,d))
            elif (b == d):
                if (i*c == j*a):
                    fractions_found.append((a,c))
    return fractions_found

def main():
    t = time.time()
    print euler_33()
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
