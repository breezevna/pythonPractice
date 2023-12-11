# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()

# matrix = [[277, -930, 11, 0],
#            [9, 43, 6, 87],
#            [4456, 8, 290, 7]]

# print_matrix(matrix,3)
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=' ')
#     print()
# n = 3
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# n1, n2 = 0,0
# for i in range(n):
#     for j in range(n):
#         n1 = n - i -1
#         n2 = n - j - 1
#         print(a[n2][n1], end=' ')
#     print()
# n = 5
# a = [[19, 21, 33, 78, 99],
#      [41, 53, 66, 98, 76],
#      [79, 80, 90, 60, 20],
#      [33, 11, 45, 67, 90],
#      [45, 67, 12, 98, 23]]

# maximum = -1
# minimum = 100

# for i in range(n):
#     if a[i][i] > maximum:
#         maximum = a[i][i]
#     if a[i][n - i - 1] < minimum:
#         minimum = a[i][n - i - 1]

# print(minimum + maximum)

matrix  = [[2, -5, -11, 0],
           [-9, 4, 6, 13],
           [4, 7, 12, -2]]

print(matrix[1][2])
