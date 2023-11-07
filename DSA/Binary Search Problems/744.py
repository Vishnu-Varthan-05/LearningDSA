def cbinarysearch(letters, target):
    if target > letters[len(letters)-1]:
            return letters[0]
    
    start_index = 0
    end_index = len(letters) - 1

    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index)//2

        if target > letters[middle_index]:
            start_index = middle_index + 1
        
        else:
            end_index = middle_index - 1

    return letters[start_index % len(letters)] 


letters = ["c", "f", "j"]
target = "c"
print(cbinarysearch(letters, target))
