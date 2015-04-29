#!/usr/bin/python
# -*- coding: utf-8 -*-

#===========================================#
#                                           #
#                                           #
#      Project Euler : probleme 186         #
#                                           #
#                                           #
#===========================================#                                           

"""
The telephone number of the caller and the called number in record n are Caller(n) = S2n-1 and Called(n) = S2n where S1,2,3,... come from the "Lagged Fibonacci Generator":

For 1 ≤ k ≤ 55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)
For 56 ≤ k, Sk = [Sk-24 + Sk-55] (modulo 1000000)

If Caller(n) = Called(n) then the user is assumed to have misdialled and the call fails; otherwise the call is successful.

From the start of the records, we say that any pair of users X and Y are friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z; and so on for longer chains.

The Prime Minister's phone number is 524287. After how many successful calls, not counting misdials, will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?
"""

# We resolve the probleme with the union-find algorithm
# We define a forest : 
# Each node know its weight, thus when we make a union we can merge the small tree under the big tree to maintain a flat tree and then increase performanace on the find part

# For union(node1,node2) : 
    # we search node1 and nodes2 parents p1 and p2 (find)
    # if p1 = p2, the node1 and 2 are connected
    # else we look at w1 and w2 the weigth of p1 and p2
    # if w1<w2 we connect p1 to p2 else p2 to p1

from collections import deque
import time


# we define the forest : 
""" forest : dictionary 
        key : int (node number)
        value : int*int (father,weigth of tree) """
forest = {}


def uninon(n1, n2):
    """ node*node -> unit : union of node1 and node1 """
    # we check if n1 and n2 are connected
    p1 = find_ancestor(n1)  # n1 ancestor , almost O(1) because trees are flat
    w1 = forest[p1][1]
    p2 = find_ancestor(n2)
    w2 = forest[p2][1]
    if p1 != p2:  # not connected
        if w1 < w2:  # we connect then p1 with p2 for keeping tress flat
            forest[p1] = (p2, w1)  # we update the father
            forest[p2] = (p2, w2+w1)  # we update the weight
        else:
            forest[p1] = (p1, w2+w1)  # we update the father
            forest[p2] = (p1, w1)  # we update the weight


def find_father(n1):
    """ int -> int: for node n find the father """
    if forest[n1][0] != -1:
        return forest[n1][0]
    else:
        return n1

def find_ancestor(n1):
    """ int -> int: for node n find the root of the tree = ancestor """
    cur = n1 # current node
    while find_father(cur) != cur:
        cur = find_father(cur) # we climb up the tree
    return cur

def prepare_forest():
    """ unit -> unit : we preapre the forest, creating one node trees """
    for i in range(0, 1000001):
        forest[i] = (-1, 1)


def generator():
    """" this generator generate the s_k number """
    queue_55 = deque()
    queue_24 = deque()
    for k in range(1, 56):
        s_k = (100003 - 200003 * k + 300007 * (k ** 3)) % 1000000
        queue_55.append(s_k)
        if k >= 32:
            queue_24.append(s_k) 
        yield s_k
    while True:
        s_k = (queue_55.popleft() + queue_24.popleft()) % 1000000
        queue_55.append(s_k)
        queue_24.append(s_k) 
        yield s_k



# 524287
""" We try to find after how many calls 99% of users will be connected to the
    PM : number 524287 """
""" to discover this we evaluate the root of the tree where the MP is 
    belonging to : it is written in the father of 524287 
    forest[find_father[524287]][1] """

def is_done():
    """ unit -> bool : do we have the 99% cluster ? """
    return forest[find_ancestor(524287)][1] >= 990000

gen = generator() # we create the generator

def euler_186():
    """ unit -> int : find the number of caller necessary to form the cluster 
    """
    res = 0 # number of succesful calls so far
    recNr = 1 # The number of the next call
    while (not(is_done())): # O(1) operation
        (caller,called) = (next(gen), next(gen)) # we get them from gen
        if caller != called: # call was successful !
            res += 1
            print "res : ", res
            # we connect two trees in the forest, if they were not in the 
            # same cluster of course
            print forest[find_ancestor(caller)]
            print forest[find_ancestor(called)]
            uninon(caller,called) # O(1) (-> thanks to flat trees)
            print forest[find_ancestor(caller)]
        recNr += 1
        print "recNr : ", recNr
    return res


def main():
    prepare_forest()
    # print find_father(524287)
    # print is_done()
    start = time.time()
    print euler_186()
    print (time.time() - start)
#   print "s_dict =", S_dict
#   print "caller_dict =", Caller_dict
#   print "called_dict =", Called_dict




#===========================#
#                           #
#         Tests             #
#                           #
#===========================#

if __name__ == '__main__':
    main()

