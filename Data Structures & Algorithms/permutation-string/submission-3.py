from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        n = len(s1)
        l, r = 0, n
        while r <= len(s2):
            curr = s2[l:r]
            curr_freq = Counter(curr)
            print(curr_freq, s1_freq)
            if curr_freq == s1_freq:
                return True
            l += 1
            r += 1
        return False