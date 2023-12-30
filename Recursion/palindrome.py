def fibbo(n, startNumber= 1, a=1, b=1):
    if startNumber == n:
        return None
    if startNumber == 1:
        print(1, end=" ")
    print(b, end= " ")
    return fibbo(n, startNumber+1, a=b, b=a+b)

fibbo(10)
# n = 6
# number = 2
# if n == 1:
#     print(1)
# elif n == 2:
#     print(1,1)
# else:
#     a = 1
#     b = 1
#     print(1,1, end= " ")
#     while (number != n):
#         c = a+b
#         print(c, end=" ")
#         a, b = b, c
#         number+=1