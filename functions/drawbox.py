# **********
# *        *
# *        *
# *        *
# *        *
# *        *	-> Should draw
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********
def draw_box():
    a = '*'
    for i in range(14):
        if i == 0:
            print(a * 10)
        elif i == 13:
            print(a * 10)
        else:
            print(a,a, sep=' '* 8)
            
draw_box()
