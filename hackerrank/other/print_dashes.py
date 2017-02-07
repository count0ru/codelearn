
import sys

n = int(input().strip())

for x in range(1,n+1): print('{:>{z}}'.format('#'*x,z=n))
