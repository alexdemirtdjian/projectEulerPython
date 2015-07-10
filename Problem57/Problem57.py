#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 57          #
#                                           #
#                                           #
#===========================================#                                           

# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?


import time
import fractions

def frac_step(n):
	""" int -> fraction : return the fraction for the nth iteration """
	step = n  # we have n step
	# we stop when step = 0
	tmp = fractions.Fraction(1)
	while step > 0:
		tmp = 1 + fractions.Fraction(1/(1 + tmp))
		step -= 1
	return tmp


def is_good_frac(f):
	""" fraction -> bool : test if fraction is has more digits on numerator than denominator"""
	return len(str(f.numerator)) > len(str(f.denominator))

def euler_57():
	""" unit -> int : find the solution of the problem """
	res = 0
	for n in xrange(1000):
		if n%100 == 0:
			print n
		if is_good_frac(frac_step(n)):
			res += 1
	return res





#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	# print frac_step(1)
	# print frac_step(2)
	# print frac_step(3)
	# print is_good_frac(fractions.Fraction(1393,985))  # True
	# print is_good_frac(frac_step(8))  # True
	print euler_57()
