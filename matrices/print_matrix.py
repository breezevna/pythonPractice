m, n = int(input()), int(input()) #m = col, n = row
matrix = [[0]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = input()


for i in range(m):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print()
