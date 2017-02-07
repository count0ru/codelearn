	#!/bin/python3

import sys
arr_temp=[]

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
total_sum = 0

for cursor in arr:
    total_sum+=cursor

print(total_sum)