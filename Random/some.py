number = input()
answer = ""
if len(number) %2 == 0:
    for i in range(1, len(number), 2):
        answer += number[i]
        answer += number[i-1]
else:
    for i in range(1, len(number), 2):
        answer += number[i]
        answer += number[i-1]
    answer += number[len(number)-1] 
print(int(answer))