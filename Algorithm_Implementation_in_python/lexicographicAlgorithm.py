# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 04:45:47 2020

@author: Nahid Ibne Akhtar

"""
"""
DESCRIPTION:
    Given a string, print all permutations of it in sorted order. For example, 
    if the input string is “ABC”, then output should be “ABC, ACB, BAC, BCA, CAB, CBA”.
    This means:
        1. It sorts the given list in non-decreasing order.
        2.Start generating next higher permutation. Do it until next higher permutation is not possible.
"""

"""
References:
    algorithm: Lexicographic algorithm
    source: 
        1. https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
        2. https://codeforces.com/contest/1328/problem/B
"""
#swaping indexed elements
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    

#Given array/list as input
#val = ['a', 'a','r','c', 'a', 'b', 'b']
val = [21, 5, 89, 32, 145, 234, 678, 987]


#Loop
for h in range(100000):

    lenVal = len(val)  
   
    largestI = -1  
    for i in range(lenVal-1):
        if val[i]<val[i+1]:
            largestI = i
        #print("2nd Largest Index of the list: ", largestI)
        
    if largestI == -1:
        print("Not found 2nd Largest, Finished!")
        break
    
    largestJ = -1
    for j in range(lenVal):
        if val[largestI]< val[j]:
            largestJ = j
        #print("y<x Index is: ", largestJ )
        

    #Call the swap Function
    swap(val, largestI, largestJ)

    #Slicing the list/array from LargestI+1 to the end and reverse it and append to the initial array  
    val[largestI+1:] = reversed(val[largestI+1:])
    print(val)



