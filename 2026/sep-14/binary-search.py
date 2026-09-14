from typing import List

arr = [3, 7, 9, 11, 12]

k = 11
l = 10


# in binary search we traverse the sorted array and compare `mid = (l + r) // 2` index element to the value we're looking for
# case 1(value at mid == value we're looking for):
# then return mid
# case 2(value at mid < value we're looking for):
# then we know that our value can only be on the right side
# of mid, so we move `l` to `mid + 1`
# case 3(value at mid > value we're looking for):
#  then we know that our value can only be on the left side
#  of mid, so we move `r` to `mid - 1`
# if `l > r`, then we have searched all possible positions
# and the value does not exist in the array


def binary_search(arr: List[int], to_find: int):

    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == to_find:
            return mid
        elif arr[mid] < to_find:
            l = mid + 1
        else:
            r = mid - 1

    return -1


print(binary_search(arr, k))  # this will give 3
print(binary_search(arr, l))  # this will give -1
