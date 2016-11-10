#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 76          #
#                                           #
#                                           #
#===========================================#                                           


# It is possible to write five as a sum in exactly six different ways:

# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1

# How many different ways can one hundred be written as a sum of at least two positive integers?


# we note phi(k) the number of different ways k can be written as a sum of at least two positive integers

# we store the phi in a dict
dict_psi = {(3,1):2}

# we note the psi(n, k) : the number of different ways k can be written as a sum of at least two positive integers greater than k
# phi(n) = sum_{k = 1}^{k = n/2}(1 + psi(n-k, k))

# psi(n, 1) = phi(n)
# psi(n, n/2) = 1

def psi(n, k):
	""" int * int -> int """
	try:
		return dict_psi[(n,k)]
	except:	
		# not suppose to happen
		if(k > (n/2)):
			return 0
		elif( k == (n/2)):
			dict_psi[(n,k)] = 1;
			return 1
		else:
			res = 0
			for i in xrange(1, (n/2)+1):
				res += (1 + psi(n - i, k+i-1))
				print res
			dict_psi[(n,k)] = res
			return res


def euler_76():
	""" unit -> int : """
	return psi(100, 1)



def main():
	# print psi(2, 1)
	# print psi(5, 1)
	# print dict_psi
	# print psi(6, 1)
	print psi(6, 2)
#	print euler_76()


#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	main()

