#!/bin/python3

#https://www.hackerrank.com/challenges/angry-professor?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=3-day-campaign

import sys

t = int(input().strip())

if (t >= 10 and t <= 0): sys.exit(0)

for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    good_students=n-len([x for x in a if x <= 1])
    print("gs:",good_students)
    if ((n >= 1  and n <= 1000) or k > n) and good_students <= k: 
        print("YES") 
    else:
        print("NO")
