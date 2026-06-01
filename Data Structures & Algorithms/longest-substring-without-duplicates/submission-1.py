class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # comparing len substr to len set of the substr
        # if equal, incr. r and update max len
        # while l < r and not equal: l += 1
        max_len = 0
        l = 0
        curr_set = set()
        for r in range(len(s)):
            while l < r and s[r] in curr_set:
                curr_set.remove(s[l])
                l += 1
            curr_set.add(s[r])
            max_len = max(max_len, (r - l + 1))
        return max_len