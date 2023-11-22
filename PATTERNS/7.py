#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
n = 5
for i in range(1, n*2):
    if i <= n:
        no_of_stars = i
        print(" "*(n - i), end ="")
    else:
        no_of_stars = n - (i - n)
        print(" "*(i - n), end ="")
    for j in range(no_of_stars):
        print("*", end='')
    print()