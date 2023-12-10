def pascal(n):
    result = []
    for i in range(n + 1):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]
        result.append(row)
    return result[n]

n = int(input())
print(pascal(n))
