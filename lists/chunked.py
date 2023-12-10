def chunked(text, n): #a b c d, 2 -> [['a', 'b'], ['c', 'd']]
    list = []
    count = 1
    for char in text.split():
        if not list or count >= n:
            list.append([char])
            count = 1
        else:
            list[-1].append(char)
            count += 1
    print(list)

chunked(input(), int(input()))

