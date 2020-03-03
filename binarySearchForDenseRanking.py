# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:00:49 2020

@author: uic38334
"""

def br(li, key, low, high):
    val = 0
    mid = (low+high)//2
#    print(low, mid, high)
    if li[mid] == key:
        val = mid+1
#        print("1")
    elif key>li[mid]:
        if mid == 0:
#            print("2A")
            val = 1
        elif li[mid-1] > key:
#            print("2B")
            val = mid + 1
        else:
#            print("2C")
            val = br(li, key, low, mid)
    else:
        if mid == len(li)-1:
#            print("3A")
            val = len(li) + 1
        elif li[mid+1]<key:
#            print("3B\t", mid)
            val = mid + 2
        else:
#            print("3C")
            val = br(li, key, mid+1, high)
#    print(val)
    return val

f = 1

while(f == 1):
    li = [100, 100, 50, 40, 40, 20, 10]
    li = list(set(li))
    li = sorted(li)
    li = li[-1::-1]
    
    n = input("Enter the value --> ")
    
    v = br(li, int(n), 0, 4)
    print(li)
    print(v)
    f = int(input("Continue? 1/0 -->"))




