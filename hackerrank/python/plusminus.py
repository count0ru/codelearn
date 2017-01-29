#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

minus,plus,zeroes = 0,0,0

for element in arr:
	if element > 0: plus+=1
	elif element < 0: minus+=1
	else: zeroes+=1

print(plus/n)
print(minus/n)
print(zeroes/n)
