# 167. Two Sum II - Input Array Is Sorted


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force two pointers
        # l = 0
        # r = len(nums) - 1

        # while l < r:
        #     if (nums[l] + nums[r]) == target:
        #         return [l+1, r+1]
        #     elif nums[l] + nums[r] < target:
        #         l += 1
        #     elif nums[l] + nums[r] > target:
        #         r -= 1
        # return []

        # two pointers with binary search
        for i in range(len(nums)):
            diff = target - nums[i]

            l = i + 1
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == diff:
                    return [i + 1, mid + 1]

                elif nums[mid] < diff:
                    l = mid + 1

                else:
                    r = mid - 1

        return []


s = Solution()
print("Example 1:", s.twoSum(nums=[2, 7, 11, 15], target=9))  # [1,2]
print("Example 2:", s.twoSum(nums=[2, 3, 4], target=6))  # [1,3]
print("Example 3:", s.twoSum(nums=[-1, 0], target=-1))  # [1,2]
