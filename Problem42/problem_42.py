#!/usr/bin/python
# -*- coding: utf-8 -*-

# ========================================================================== #
#                                                                            #
#                                                                            #
#      				   Project Euler : probleme 42        			 	     #
#                                                                            #
#                                                                          	 #
# ========================================================================== #


# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
# so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its 
# alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word 
# value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
# containing nearly two-thousand common English words, how many are triangle words?


import time


with open('p042_words.txt', 'r') as words:
    # we open the file with a "with" statement, cleaner way, do not need 
    # to close it
    all_words = words.read()
    words_list = all_words.split('","')
    # words_list, the list of the words.


triangular_list = [((n+1)*n)/2 for n in xrange(1, 1000)]

def is_triangular_words(s):
    """ string -> bool : check if s is a triangular word """
    l = []  # a list containing all characters
    for i in s:
        l += [i]
    # all the string are upperase
    # ord('A') = 65, ord('B') = 66 ...
    g = lambda c: ord(c) - 64
    # g : char -> int, return the value of the char
    s_value = sum(map(g, l))
    return(s_value in triangular_list)
    

def euler_42():
    """ unit -> int : resolve problem euer 42, count the triangular words """
    res = 0  # number of triangular words
    for s in words_list:
        if is_triangular_words(s):
            res += 1
    return res


def main():
    # print is_triangular_words("SKY")  # True
    # print len(words_list)  # 1788
    t = time.time()
    print euler_42()
    print time.time() - t

# =========================== #
#                             #
#           Tests             #
#                             #
# =========================== #

if __name__ == '__main__':
    main()
