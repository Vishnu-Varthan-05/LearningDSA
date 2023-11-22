def bubble(array):
    for i in range(len(array)):
        for j in range(1, len(array)-i):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
    return array

array = [6, 7 ,10, 1, 5, 0]
print(bubble(array))