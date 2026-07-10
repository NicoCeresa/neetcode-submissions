class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram -> same number of each letter
        if len(s) != len(t):
            return False

        count_s = {}
        for l in s:
            if l not in count_s:
                count_s[l] = 1
            else:
                count_s[l] += 1

        for l in t:
            if l not in count_s:
                return False
            count_s[l] -= 1
            if count_s[l] == 0:
                del count_s[l]
        return len(count_s) == 0