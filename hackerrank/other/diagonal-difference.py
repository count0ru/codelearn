
n = int(input().strip())

a_diagonal, b_diagonal = 0,0

for i in range(n):
	row = [int(row_element) for row_element in input().strip().split(' ')]
	a_diagonal += row[i]
	b_diagonal += row[n-1-i]

print(abs(a_diagonal - b_diagonal))