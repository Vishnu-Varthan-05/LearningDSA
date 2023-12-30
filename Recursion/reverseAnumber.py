# n = 1234
# reversed = 0
# while n != 0:
#     reversed = reversed*10 + n%10
#     n//=10
# print(reversed)

def reverseTheNumber(n, reversed = 0):
    if n == 0:
        return reversed
    return reverseTheNumber(n//10, reversed*10 + n%10)

print(reverseTheNumber(1234))