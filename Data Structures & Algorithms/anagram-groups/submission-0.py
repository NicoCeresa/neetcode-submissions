class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group anagrams into 2 sublists
        # loop once and create counters
        # if counters same then add to list
        out = defaultdict(list)
        for char in strs:
            count = [0] * 26
            for c in char:
                count[ord(c) - ord('a')] += 1
            out[tuple(count)].append(char)
        return list(out.values())