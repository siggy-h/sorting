#!/usr/bin/python
# Copyright (c) Siggy Hinds
#
# This program analyzes the running time of different sorting algoritms.
#

import random
from timeit import default_timer as timer


def main():
    size = 10   # number of list elements
    myList = []

    random.seed() # uses system time as seed

    # make a list of sortable items
    for i in range(0, size):
         myList.append( random.randint(0,50) )

    printList('The list:', myList)

    pySortList = list(myList) # copy original list
    mergeSortList = list(myList) # copy original list

    # time python's list sort()
    start = timer()
    pySortList.sort();
    end = timer()
    print("Time - Python list sort: ", end - start)
    printList('pySortList:', pySortList)

    # time merge sort
    start = timer()
    newMergedList = mergeSort(mergeSortList)
    end = timer()
    print("Time - Merge Sort: ", end - start)
    printList('merged list:', newMergedList)



def printList(msg, aList ):
    if msg != '':
        print msg

    x = [i for i in aList]
    print x



##############################
###   SORTING ALGORITHMS   ###
##############################

def mergeSort( aList ):
    # input a list, returns a permutaion of the list in non-decreasing order
    n = len(aList)
    if n == 1:
        return aList

    mid = n/2
    B = mergeSort( aList[:mid] )
    C = mergeSort( aList[mid:] )
    return merge(B, C)

def merge(B, C):
    # input two lists, returns one list that combines left & right
    A = []
    i = 0
    j = 0

    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            A.append(B[i])
            i += 1
        else:
            A.append(C[j])
            j += 1
    if i == len(B):
        A.extend(C[j:])
    else:
        A.extend(B[i:])

    return A



# Python formalism
if __name__ == "__main__":
    main()
