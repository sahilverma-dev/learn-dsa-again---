class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        nums_set = set(nums)

        max_length = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current_length += 1
            elif nums[i] != nums[i-1]:
                max_length = max(max_length, current_length)
                current_length = 1

        return max(max_length, current_length)


s = Solution()


print("Example 1:", s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))  # 4
print("Example 2:", s.longestConsecutive(
    nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print("Example 3:", s.longestConsecutive(nums=[1, 0, 1, 2]))  # 3
