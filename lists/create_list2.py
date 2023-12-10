def create_list(n):
    my_list = []
    i = 0
    for i in range(1, int(n) + 1):
        my_list = [int(i) for i in range (1, i + 1)]
        print(my_list)

create_list(input())
