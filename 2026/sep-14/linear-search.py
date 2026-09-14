from typing import List

arr = [7, 12, 9, 11, 3]

k = 11
l = 10

# in linear search we traverse the array(can be unsorted) and find for the index of the element linearly


def linear_search(arr: List[int], to_find: int):
    for i, el in enumerate(arr):
        if el == to_find:
            return i
    return -1


print(linear_search(arr, k))  # this will give index of element
print(linear_search(arr, l))  # this will give -1
