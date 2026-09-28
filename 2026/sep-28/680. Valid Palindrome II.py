# 680. Valid Palindrome II


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (
                    is_palindrome(left + 1, right)
                    or is_palindrome(left, right - 1)
                )

        return True


s = Solution()


# True
print("Example 1: ", s.validPalindrome(s="aba"))
print("Example 2: ", s.validPalindrome(s="abca"))  # True
print("Example 3: ", s.validPalindrome(s="abc"))  # False
