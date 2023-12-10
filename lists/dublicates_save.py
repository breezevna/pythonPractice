def duplicate_save(text):
    list = []
    for char in text.split():
        if not list or char != list[-1][-1]:
            list.append([char])
        else:
            list[-1].append(char)
    print(list)

duplicate_save(input()) #a b c d
