#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 52          #
#                                           #
#                                           #
#===========================================#       

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


import time
import operator
import collections

# define a function that given two lists compare the equality with cardinality
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)


def same_digits(n1, n2):
	""" int * int -> bool : check if the two integers contains the same digits """
	return compare(list(str(n1)), list(str(n2)))

def is_sol(n):
	""" int -> bool : chack if n is a solution """
	# We abort as soon as a k*n is not a good number in order to minimise the tests
	if same_digits(n, 2*n):
		if same_digits(n, 3*n):
			if same_digits(n, 4*n):
				if same_digits(n, 5*n):
					return same_digits(n, 6*n)
				return False
			return False
		return False
	return False

def euler_52():
	""" unit -> int : find the soliution """
	cur = 1
	while (not is_sol(cur)):
		cur += 1
	return cur




#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	print same_digits(125874, 251748) # True 
	print same_digits(11112, 22221) # False
	print same_digits(1111, 111) # False
	print same_digits(11223, 32112) # True
	print euler_52()
