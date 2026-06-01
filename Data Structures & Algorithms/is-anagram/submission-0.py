class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count_s = {}
        for idx, char in enumerate(s):
            count_s[char] = count_s.get(char, 0) + 1
        print(count_s)

        for char in t:
            if char not in count_s or count_s[char] <= 0:
                return False
            else:
                count_s[char] -= 1
        return True