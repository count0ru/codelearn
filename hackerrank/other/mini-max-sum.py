numbers =  [int(x) for x in input().split()]
results = []
i = 0

for element in numbers:
    results.append(sum(numbers)-element)
    
print(min(results),max(results))
    
