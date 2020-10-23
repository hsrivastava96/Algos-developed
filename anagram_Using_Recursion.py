# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:39:36 2020

@author: Harshit Srivastava
"""

def anagram(arr, i):
#    print("Start", arr, i)
    if(i == len(arr)):
        print(arr)
    else:
        for j in range(i, len(arr)):
#            print("J = ", j, arr)
            s_A = [x for x in arr]
            temp = s_A[i]
            s_A[i] = s_A[j]
            s_A[j] = temp
            anagram(s_A, i+1)


anagram(['A', 'B', 'C', 'D'], 0)    
