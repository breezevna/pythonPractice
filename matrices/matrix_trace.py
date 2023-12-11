n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

sum = 0
for i in range(n):
    sum += matrix[i][i]
print(sum)
