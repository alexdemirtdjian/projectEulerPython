#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 79          #
#                                           #
#                                           #
#===========================================#                                           


# A common security method used for online banking is to ask the user for three random 
# characters from a passcode. For example, if the passcode was 531278, they may ask for 
# the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the file so as 
# to determine the shortest possible secret passcode of unknown length.

keylog = [ 319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 
	168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 
	162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]

def to_list(n):
	""" int -> int list """
	return map(lambda s: int(s), list(str(n)))

def attemp_match(n, attemp):
	"""
	int * int -> bool
	test if the attemp is subpart of the n number
	"""
	array_n = to_list(n)
	array_attemp = to_list(attemp)
	res = True
	cursor = -1 # keep track of order we find the digits
	for i in array_attemp:
		try:
			# we search for the next position of the current digit in the subarray 
			# from position cursor+1 to the end
			cursor = array_n[(cursor+1):].index(i)  # update position
		except:
			# value Error not in the array
			return False
	return True

def attemps_match(n, attemps_list):
	""" int * int list -> bool """
	res = True
	cur = 0
	while(res and (cur < len(attemps_list))):
		res = attemp_match(n, attemps_list[cur])
		cur += 1 # next word
	return res


def project_euler_79():
	"""
	unit -> int
	"""
	res = 0
	while(True):
		if attemps_match(res, keylog):
			return res
		else:
			res += 1
			print res

	










#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	print to_list(121343)	# [1, 2, 1, 3, 4, 3]
	print attemp_match(123456789, 4689)	# True
	print attemp_match(123456789, 4692)	# False
	print attemps_match(123456789, [469, 123, 456, 146])	# True
	print project_euler_79()


