#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 206         #
#                                           #
#                                           #
#===========================================#                                           



"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

def decompose(n):
	""" int->int list : decompose un entier dans une liste 
	decompose(34) = [3,4]"""
	if (n<=9):
		return [n]
	else:
		# par recurrence
		a = n % 10 
		b = (n-a)/10
		l = decompose(b)
		return l+[a]

def is_matching(l):
	""" int list -> bool : teste si il y a match sur les deux list """
	if (len(l) != 19):
		return False
	# test sur l[0..-1]
	for i in range(9):
		if (l[2*i] != (i+1)):
			return False # on sort du while
	# test sur la derniere valeur
	if l[18] != 0:
		return False 
	# on a passe tous les tests c'est ok
	return True


l2 = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,0]

def euler_205():
	""" unit->int """
	res = 10**9 # resultat provisoire
	while (not is_matching(decompose(res**2))):
		res +=10 # 10 divise res**2 
		print(res)
	return res



"""
Encadrement de x
10**18 < x**2 < 2*10**18
10**9 < x < sqrt(2)*10**9

"""
def main():
	print decompose(56)
	print is_matching(l2)
	# Tests sur certains carrees pour encadrer sur deux valeurs
	print (len(decompose((10**9)**2))) # 19
	print (len(decompose((2*10**9)**2))) # 19
	print(euler_205())




#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	main()

