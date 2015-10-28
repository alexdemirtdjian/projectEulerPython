#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                      									     #
#                 									                         #
#      				   Project Euler : probleme 55        			 	     #
#                                           						         #
#                                           						    	 #
# ========================================================================== #

# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

# Not all numbers produce palindromes so quickly. For example,

# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337

# That is, 349 took three iterations to arrive at a palindrome.

# Although no one has proved it yet, it is thought that some numbers, like 196, 
# never produce a palindrome. A number that never forms a palindrome through the 
# reverse and add process is called a Lychrel number. Due to the theoretical nature 
# of these numbers, and for the purpose of this problem, we shall assume that a number 
# is Lychrel until proven otherwise. In addition you are given that for every number 
# below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, 
# or, (ii) no one, with all the computing power that exists, has managed so far to map it 
# to a palindrome. In fact, 10677 is the first number to be shown to require over fifty 
# iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

# How many Lychrel numbers are there below ten-thousand?

# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.


# we store the palindrome in this dict not to recalculate all iteration
palindrome_dict = {}

def is_palindrome_aux(n, iteration_remaining):
    """ int * int -> bool : check if n on the kth iteration is a palindrome  """
    if (iteration_remaining == 0):
        return False
    else:
        # store in next_n the reverse and add sum
        next_n = n + int(''.join(list(str(n))[::-1]))

        l1 = list(str(next_n))
        l2 = l1[::-1]
        # if we have a palindrome
        if(l1 == l2):
            return True
        else:
            return is_palindrome_aux(next_n, iteration_remaining - 1)


def is_palindrome(n):
    """ int -> bool : check if n is is a palindrome in less than 50 iteration """
    return is_palindrome_aux(n, 50)

def euler_55():
    """ unit -> int """
    res = 0
    for i in xrange(1, 10**4 + 1):
        if not(is_palindrome(i)):
            res+=1
    return res


def main():
    print is_palindrome_aux(47, 10)  # True
    print is_palindrome_aux(349, 10)  # True
    print is_palindrome_aux(349, 1)  # False
    print is_palindrome(349)  # True
    print is_palindrome(4994)  # False

    print euler_55()


# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
