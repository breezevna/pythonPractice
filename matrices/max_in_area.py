n = int(input())
matrix = []
for i in range(n):
    elements = [int(num) for num in input().split()]
    matrix.append(elements)

maximum = float('-inf')
for i in range(n):
    for j in range(n):
        if i >= j and i <= n - j -1 or i <= j and i >= n - 1 - j:
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
print(maximum)
