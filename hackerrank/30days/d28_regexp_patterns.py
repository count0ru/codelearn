#!/bin/python3

import sys

database = {}

N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    database[str(firstName)] = str(emailID)

for w in sorted(database):
      print(w)

