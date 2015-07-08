#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 31          #
#                                           #
#                                           #
#===========================================#                                           


"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def match_sum(l):
	""" int list -> bool : test si la somme relative aux nombre de piece vaut 200p"""
	res = 0
	for k in range(8):
		res += pieces[k]*l[k]
	return res == 200


def combinaison(somme, pieces):
	""" int* int list -> int : 
		combinaison(x, pieces) calcul le nombre de combinaison pour obtenir x avec les pieces """
	# cas d'arret de la recurrence
	if(len(pieces) == 1):
		a =  pieces[0]
		if ((somme % a) == 0):
			return 1
		else:
			return 0
	# cas d'arret sur la somme
	if(somme <= 0):
		return 0
	# par recurrence
	piece = pieces[-1]
	n1 = combinaison(somme,[piece]) # on cherche avec la derniere piece
	n2 = combinaison(somme,pieces[0:-1]) # on cherche sans la derniere pieces
	# on melange la derniere piece avec les autres
	n3 = 0 # initialisation a 0
	b = pieces[-1] # la derniere piece de la liste (200 pour le premier tour par expl)
	somme_aux = somme-b # on decremente la somme
	while(somme_aux>0):
		n3+=combinaison(somme_aux,pieces[0:-1])
		somme_aux-=b
	return(n1+n2+n3)



def euler_31():
	""" unit->int : le resultat du probleme"""
	return combinaison(200,pieces)


def main():
	print match_sum([3,1,1,0,2,1,1,0]) #True : exemple de matching
	print(combinaison(10,[1,2,5]))
	print(euler_31())






#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	main()

