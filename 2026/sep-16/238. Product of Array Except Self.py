class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # ans = []

        # totalProduct = 1

        # for i in nums:
        #     totalProduct *= i
        # print(totalProduct)

        # for i in nums:
        #     if (i != 0):
        #         ans.append(totalProduct//i)
        #         # print(i, totalProduct//i)

        # return ans
        n = len(nums)

        prefix_product_array = [1] * n
        postfix_product_array = [1] * n

        prefix_product = 1
        postfix_product = 1

        # Prefix
        for i in range(n):
            prefix_product_array[i] = prefix_product
            prefix_product *= nums[i]

        # Postfix
        for i in range(n - 1, -1, -1):
            postfix_product_array[i] = postfix_product
            postfix_product *= nums[i]

        ans = []

        for i in range(n):
            ans.append(
                prefix_product_array[i] *
                postfix_product_array[i]
            )

        return ans


s = Solution()


print("Example 1:", s.productExceptSelf(nums=[1, 2, 3, 4]))  # [24,12,8,6]
print("Example 2:", s.productExceptSelf(nums=[-1, 1, 0, -3, 3]))  # [0,0,9,0,0]
