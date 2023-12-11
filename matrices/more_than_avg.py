n = int(input())
matrix = []
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    avg = 0
    count = 0
    for j in range(n):
        avg += matrix[i][j]
    avg = avg/n
    for k in range(n):
        if avg < matrix[i][k]:
            count += 1
    print(count)
