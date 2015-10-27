#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 85          #
#                                           #
#                                           #
#===========================================#                                           



# we note phi(n, m) : the nuumber of rectangle that can fit inside an n x m grid
# we notice the recurrent relation
# phi(n + 1, m) = 2 * phi(n, m) - phi(n - 1, m) + mx(m + 1)/2
# phi(n, m + 1) = 2 * phi(n, m) - phi(n, m - 1) + (1 + ... + n)
# 
# number of rectangles inside grid (n+1)xm
# 	number of rectangle touching left side : l
# 	number of rectangle touching right side : r
# 	number of rectangle not touching any side : c
# 	number of rectangle touching both side : b
#	-> phi(n+1, m) = l + r + c + b
# 	l + c = r + c = phi(n, m)
#	c = phi(n - 1, m)
# 	b = 1 + 2 + ... + m = mx(m + 1)/2
#	-> phi(n + 1, m) = 2 x phi(n, m) - phi(n - 1, m) + (1 + 2 + ... + m)

import sys
sys.setrecursionlimit(20000)

# dict containing calculated phi (not to calculate two times)
phi_dict = {}


def phi(n, m):
	""" int * int -> int : number of rectancgle inside n x m grid """
	try:
		return phi_dict[(n, m)]
	except:
		if(n == 0):
			phi_dict[(n,m)] = 0
			return 0
		elif(n == 1):
			phi_dict[(n,m)] = (m * (m + 1)/2)
			return (m * (m + 1)/2)
		else:
			res = 2 * phi(n - 1, m) - phi(n - 2, m) + (m * (m + 1)/2)
			phi_dict[(n,m)] = res
			return res

def euler_85():
	""" unit -> int : area of the grid with nearest 2 000 000 rectancgles """
	res = (0,[0,0])
	best_distance = 2000000  # difference btw current grid nb of rectangle and 2000000
	for n in xrange(2000):
		for m in xrange(2000):
			current_distance = abs(phi(n,m) - 2000000)
			if(current_distance < best_distance):
				res = (n*m,[n,m])
				best_distance = current_distance
	return res












def main():
	# some checks
	print(phi(3, 2))  # 18 ok
	print(phi(2, 3))  # 18 ok
	print(phi(1, 2))  # 3 ok
	print(phi_dict)
	print(phi(150, 50))
	print(phi_dict)
	print(phi(2000, 1))  # 2001000
	print(euler_85())
	print(phi(36,77))  # 1999998 : solution -> 36x77 = 2772

	



#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	main()

