def numberOfzeros(n, answer=0):
    if n == 0:
        return answer
    elif n%10 == 0:
        return numberOfzeros(n//10, answer+1)
    return numberOfzeros(n//10, answer)

print(numberOfzeros(300))