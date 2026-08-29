from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - all anagrams into sub-lists
        - maybe some sort of counts?
        - ordinal encoding?
        """
        char_map = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for char in s:
                char_ord = ord(char) - ord("a")
                chars[char_ord] += 1
            char_map[tuple(chars)].append(s)            
        return list(char_map.values())