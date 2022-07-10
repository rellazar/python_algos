import random

def shuffle(arr):
    new_arr = []
    for i in range(len(arr)):
        random_index = random.randint(0, len(arr) - 1)
        new_arr.append(arr[random_index])
        arr.pop(random_index)
    return new_arr

print(shuffle([13,16,8,24,12,21]))


def skyline(arr):
    new_arr = []
    last_tallest = 0
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] > last_tallest:
            new_arr.append(arr[i])
            last_tallest = arr[i]
        print(new_arr)
        print(last_tallest)

skyline([-1, 1, 1, 7, -5, 3])
skyline([0,4])


def zip_it(arr1, arr2):
    larger_arr = arr1 if len(arr1) > len(arr2) else arr2
    new_arr =[]
    for i in range(len(larger_arr)):
        if i <= (len[arr1]) -1:
            new_arr.append(arr1[i])
        if i  <= (len[arr2]) -1:
            new_arr.append(arr2[i])
    return new_arr