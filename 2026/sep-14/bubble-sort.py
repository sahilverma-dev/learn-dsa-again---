arr = [7, 12, 9, 11, 3]

print("Before Sort:")
print(arr)

# bubble sort
n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        # check if j i smaller then j+1 element
        if arr[j] > arr[j + 1]:
            # then swap the elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # print(i, arr[i])

print("After Sort:")
print(arr)
