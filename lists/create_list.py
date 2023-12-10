def create_list(n):
    my_list = []
    for i in range(int(n)):
        my_list = [int(i) for i in range(1, int(n) + 1)]
        print(my_list)
create_list(input())
