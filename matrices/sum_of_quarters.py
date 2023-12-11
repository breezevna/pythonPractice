n = int(input())
matrix = []
for i in range(n):
    elements = [int(num) for num in input().split()]
    matrix.append(elements)

sum_up, sum_down, sum_left, sum_right = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if i > j and i < n - j - 1:
            sum_left += matrix[i][j]
        if i < j and i > n - j - 1:
            sum_right += matrix[i][j]
        if i< j and i < n - j - 1:
            sum_up += matrix[i][j]
        if i > j and i > n - j - 1:
            sum_down += matrix[i][j]
print('Верхняя четверть:', sum_up)
print('Правая четверть:', sum_right)
print('Нижняя четверть:', sum_down)
print('Левая четверть:', sum_left)
