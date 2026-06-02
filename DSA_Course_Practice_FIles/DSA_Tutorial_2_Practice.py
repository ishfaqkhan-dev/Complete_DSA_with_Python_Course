
# numbers = [3, 1, 4, 1, 5]

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         print(numbers[i], numbers[j])


# Binary search example
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

target = 13
low = 0
high = len(numbers) - 1

while low <= high:
    mid = (low + high) // 2
    if numbers[mid] == target:
        print("Found at index", mid)
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1