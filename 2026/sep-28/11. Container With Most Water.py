# 11. Container With Most Water

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # We cannot simply choose the two largest heights.
        # Why?
        #
        # Area = width * height
        # width = distance between the two indexes
        # height = smaller of the two lines
        #
        # So the position (index) of a line also matters.
        #
        # Example:
        # height = [10, 1, 1, 1, 1, 9]
        #
        # The two largest heights are 10 and 9.
        # Their indexes are 0 and 5.
        # Area = (5 - 0) * min(10, 9)
        #      = 5 * 9
        #      = 45
        #
        # But in general, choosing the two largest heights
        # does NOT guarantee the largest area.
        #
        # Therefore, for the brute-force solution,
        # we try every possible pair of indexes.

        # max_area = 0

        # # Choose the first line
        # for i in range(len(height)):

        #     # Choose the second line
        #     for j in range(i + 1, len(height)):

        #         # Distance between the two lines
        #         width = j - i

        #         # The container can only hold water up to
        #         # the height of the shorter line.
        #         h = min(height[i], height[j])

        #         # Calculate the area for this pair
        #         area = width * h

        #         # Keep the largest area we have found
        #         max_area = max(max_area, area)

        # return max_area

        # two pointers brture force this will work but not submit due to Time Limit Exceeded

        # ans = 0
        # n = len(height)

        # for l in range(n):
        #     for r in range(l+1,n):
        #         area = (r-l) * min(height[l] ,height[r] )
        #         ans = max(ans,area)

        # return ans
        n = len(height)
        ans = 0
        l = 0
        r = n - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            ans = max(ans, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans


s = Solution()


# 49
print("Example 1: ", s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
print("Example 2: ", s.maxArea(height=[1, 1]))  # 1
