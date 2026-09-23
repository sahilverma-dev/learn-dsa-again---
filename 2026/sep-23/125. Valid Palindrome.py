class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


s = Solution()

print("Example 1:", s.isPalindrome(s="A man, a plan, a canal: Panama"))  # True
print("Example 2:", s.isPalindrome(s="race a car"))  # False
print("Example 3:", s.isPalindrome(s=" "))  # True
