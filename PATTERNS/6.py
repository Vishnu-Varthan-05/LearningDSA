# *
# **
# ***
# ****
# ***
# **
# *
# for i in range(1, 8):
#     if i <= 4:
#         no_of_stars = i
#     else:
#         no_of_stars = 4 - (i - 4) 
#     for j in range(no_of_stars):
#         print("*", end='')
#     print()

# n = 5
# for i in range(1, n*2):
#     if i <= n:
#         no_of_stars = i
#     else:
#         no_of_stars = n - (i - n) 
#     for j in range(no_of_stars):
#         print("*", end='')
#     print()

n = 5
for i in range(1, n*2):
    if i <= n:
        for j in range(i):
            print("*", end='')
    else:
        for j in range(n - (i - n)):
            print("*", end='') 
    print()
