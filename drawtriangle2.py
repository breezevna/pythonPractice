# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
def draw_triangle(fill, base):
    for i in range(1,base+1):
        for j in range(i):
            if i + j <= base:
                print(fill, end='')
        print()

print("Enter the symbol to draw")
a = input()
print("Enter the base")
b = int(input())
draw_triangle(a,b)

