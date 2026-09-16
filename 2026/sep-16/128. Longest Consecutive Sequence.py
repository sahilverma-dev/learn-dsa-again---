class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # if not nums:
        #     return 0

        # nums.sort()

        # max_length = 1
        # current_length = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1] + 1:
        #         current_length += 1
        #     elif nums[i] != nums[i-1]:
        #         max_length = max(max_length, current_length)
        #         current_length = 1

        # return max(max_length, current_length)

        # O(n)
        ans = 0

        numsSet = set(nums)

        for i in numsSet:
            # check if i is the start of a sequence
            if (i-1) not in numsSet:
                length = 0
                while (i+length) in numsSet:
                    # this loop only starts when i is the first number of a consecutive sequence.
                    # The `while` loop is **not O(1)** by itself; for a consecutive sequence of length `k`, it can run `k` times, making it **O(k)**. However, the overall algorithm is still **O(n)** because the `if (i - 1) not in numsSet` condition ensures that the `while` loop only starts at the beginning of a sequence, and each number is visited by a `while` loop at most once across the entire algorithm. So even though one `while` loop may run many times, the **total number of `while` iterations across all sequences is at most `n`**, giving `O(n)` overall time (with `O(1)` average set lookups).

                    length += 1
                ans = max(ans, length)

        return ans


s = Solution()


print("Example 1:", s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))  # 4
print("Example 2:", s.longestConsecutive(
    nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
print("Example 3:", s.longestConsecutive(nums=[1, 0, 1, 2]))  # 3
