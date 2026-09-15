from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # first compare the length
        n = len(s)
        m = len(t)

        if (n != m):
            return False

        count_dict = defaultdict(int)

        for c in s:
            count_dict[c] += 1

        for c in t:
            count_dict[c] -= 1

        # print(count_dict)
        if any(count_dict.values()):
            return False
        else:
            return True


s = Solution()


print("Example 1", s.isAnagram(s="anagram", t="nagaram"))  # true
print("Example 2", s.isAnagram(s="rat", t="car"))  # false
