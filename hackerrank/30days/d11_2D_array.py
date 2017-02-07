import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


total = 0
a_max = []

for i in range(len(arr)-2):
    i = int(i)
    for x in range(len(arr)-2):
        x = int(x)
        total = sum(arr[i][x:x+3]) + int(arr[i+1][x+1]) + sum(arr[i+2][x:x+3])
        a_max.append(total)

print(max(a_max))
