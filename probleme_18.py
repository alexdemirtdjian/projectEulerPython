#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 18          #
#                                           #
#                                           #
#===========================================#                                           


 
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom of the triangle below:
# 
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23



w = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# m est une liste de liste tel que m[i][j] soit la valeur maximale que l'on puisse obtenir à la case (i,j) du triangle
m = [[0]*(i+1) for i in range(15)]


# Chiffre en ligne k (partant de 0) position l (appartenant a 0-k) : int(w[(3*k*(K+1)/2 + 3*l + 1) :(3*k*(K+1)/2 + 3*l + 3)])
def chiffre(k,l):
	""" int * int -> int """
	return(int(w[(3*k*(k+1)/2 + 3*l + 1) :(3*k*(k+1)/2 + 3*l + 3)]))


# On connait m aux bords
m[0][0] = 75
for i in range(1,15):
	for j in range(i+1):
		m[i][0] += chiffre(j,0)
		m[i][i] += chiffre(j,j)


def calcul(i,j):
	""" int*int -> int : calcul de m[i][j] à l'aide d'une formule de recurrence """
	if (m[i][j] != 0):
		return(m[i][j])
	else:
		res = chiffre(i,j) + max(calcul(i-1,j),calcul(i-1,j-1))
		m[i][j] = res # MAJ de m
		return(res)


def euler_18():
	""" unit -> int : donne le resultat du chemin maximal """
	down = [] # liste contenant les resultats du bas
	for j in range(15):
		down = down + [calcul(14,j)]
	return(max(down))







#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
	print(m)
	print("\n")
	print("la valeur recherchee est %s" %euler_18())
	
