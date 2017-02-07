#!/bin/python3

import sys
def bubbleSort(alist):
    passes_count = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                passes_count += 1
    print("Array is sorted in {} swaps.".format(passes_count))
    print("First Element: {}".format(alist[0]))
    print("Last Element: {}".format(alist[len(alist)-1]))


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
bubbleSort(a)