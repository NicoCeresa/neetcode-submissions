from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - all anagrams into sub-lists
        - maybe some sort of counts?
        - ordinal encoding?
        """
        char_map = defaultdict(list)
        for _str in range(len(strs)):
            chars = [0] * 26
            for char in strs[_str]:
                char_ord = ord(char) - 97
                chars[char_ord] += 1

            char_map[tuple(chars)].append(strs[_str])            
        return list(char_map.values())