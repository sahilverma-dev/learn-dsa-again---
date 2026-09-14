arr = [7, 12, 9, 11, 3]

print("Insertion Sort!")
print("Before Sort:")
print(arr)

# take first value of the unsorted part of the array and put it into its correct position
# do this to the unsorted part of the array till array gets sorted

# insertion sort
n = len(arr)

for i in range(1, n):
    insert_index = i
    current_value = arr.pop(i)

    for j in range(i - 1, -1, -1):
        if arr[j] > current_value:
            insert_index = j

    arr.insert(insert_index, current_value)


print("After Sort:")
print(arr)
