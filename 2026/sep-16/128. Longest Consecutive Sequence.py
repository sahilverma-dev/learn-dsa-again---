class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sorted_array = sorted(nums)

        print(sorted_array)

        return 0


s = Solution()


print("Example 1:", s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))  # 4
# print("Example 2:", s.longestConsecutive(
#     nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
# print("Example 3:", s.longestConsecutive(nums=[1, 0, 1, 2]))  # 3
