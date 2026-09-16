from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # mapping = {}
        # for str in strs:
        #     sorted_str = ''.join(sorted(str))

        #     if sorted_str in mapping:
        #         mapping[sorted_str].append(str)
        #     else:
        #         mapping[sorted_str] = [str]

        # return list(mapping.values())

        # with defaultdict
        mapping = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            mapping[key].append(word)

        return list(mapping.values())


s = Solution()

print("Example 1:", s.groupAnagrams(
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]

print("Example 2:", s.groupAnagrams(strs=[""]))
# [[""]]
