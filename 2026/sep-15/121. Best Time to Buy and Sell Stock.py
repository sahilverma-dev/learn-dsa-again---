class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # brute force
        # ans = 0

        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         diff = prices[j] - prices[i]
        #         ans = max(ans, diff)

        # return ans
        # two pointers

        max_profit = 0

        l = 0
        r = 1

        n = len(prices)

        while r < n:
            if prices[l] > prices[r]:
                l += 1
                # r += 1
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
                r += 1

        return max_profit


s = Solution()

print("Example 1", s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))  # 5
print("Example 2", s.maxProfit(prices=[7, 6, 4, 3, 1]))  # 0
print("Example 3", s.maxProfit(prices=[2, 1, 2, 1, 0, 1, 2]))  # 2
