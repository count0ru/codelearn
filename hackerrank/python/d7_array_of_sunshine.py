n = int(input().strip())

arr = [str(arr_temp) for arr_temp in input().strip().split(' ')]
#print(" ".join([str(arr[-x]) for x in range(1,len(arr)+1)]))
#print(" ".join(arr[::-1]))
print(" ".join(reversed(arr)))



