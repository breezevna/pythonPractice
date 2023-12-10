def digit_sum(num):
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    print(sum)

digit_sum(input())
