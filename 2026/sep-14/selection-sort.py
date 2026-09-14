arr = [7, 12, 9, 11, 3]

print("Selection Sort!")
print("Before Sort:")
print(arr)

# go throw the array
# move the smallest element to the front of unsorted part of the array
# repeat this again and again till array gets sorted

# selection sort
n = len(arr)
for i in range(n - 1):
    min_index = 1
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

        min_value = arr.pop(min_index)
        arr.insert(i, min_value)


print("After Sort:")
print(arr)
