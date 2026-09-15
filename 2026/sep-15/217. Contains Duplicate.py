from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


s = Solution()

print("Example 1", s.containsDuplicate([1, 2, 3, 1]))  # true
print("Example 2", s.containsDuplicate([1, 2, 3, 4]))  # false
print("Example 3", s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # true
