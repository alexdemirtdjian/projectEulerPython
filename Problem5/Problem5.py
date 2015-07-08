#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 5           #
#                                           #
#                                           #
#===========================================#                                           



# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

def test_euler(n,k):
	"""
	int * int -> bool : verification que n est bien divisible par tous les entier entre 1 et k
	"""
	res = True
	i = 1
	while res and (i < (k+1)):
		res = res and ((n % i) == 0)
		i +=1
	return(res)

def euler_5():
	n = 2520 # On initialise a 2520 le premier entier superieur a 2520 divisible aussi par 20 (Cf enonce)
	while not(test_euler(n,20)):
		n += 20 # Necessairement n est divisible par 20 donc on increment au mieux de 20
	return(n)

def main():
	start_time = time.time()
	print("La reponse au probme est", euler_5())
	print("Temps d'execution : ", time.time() - start_time, "secondes" )






#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	print("verification pour 2520")
	print(test_euler(2520,10))
	print("\n")
	main()



