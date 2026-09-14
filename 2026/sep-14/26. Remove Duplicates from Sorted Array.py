from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # we need to remove in-place duplicate elements
        # we'll use two pointer
        # l=0,r=1
        # since we've a sorted array we can increase r till we find find different value then nums[l] (r=r+1)
        # if we find different value then change the value of nums[l] to nums[r]

        if not nums:
            return 0

        l = 0

        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]

        return l + 1


s = Solution()
print("Example 1:", s.removeDuplicates(nums=[1, 1, 2]))  # Output: 2, nums = [1,2,_]
print(
    "Example 2:", s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
)  # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
