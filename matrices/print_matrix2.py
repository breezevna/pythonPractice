m, n = int(input()), int(input()) #m = col, n = row
matrix = [[0]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = input()


for i in range(m):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()

print()

transposed_matrix = []
for j in range(n):
    transposed_row = []
    for i in range(m):
        transposed_row.append(matrix[i][j])
    transposed_matrix.append(transposed_row)

for row in transposed_matrix:
    print(' '.join(row))
