class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        - true if: s and t are anagrams
        - anagram: contains same letters, diff order
        1: create counter for s
        2: iter through t, decrememnt s_counter
        3: return len(s_counter) == 0
            anagram if nothing left
            something left means that there is some difference b/w the two
        """
        # 1: count s
        count_s = {}
        for idx in range(len(s)):
            curr_char = s[idx]
            if curr_char not in count_s.keys():
                count_s[curr_char] = 1
            else:
                count_s[curr_char] += 1

        # 2: iter through t and decrement
        for idx in range(len(t)):
            curr_char = t[idx]
            if curr_char not in count_s.keys():
                return False
            else:
                count_s[curr_char] -= 1
                if count_s[curr_char] == 0:
                    del count_s[curr_char]

        return len(count_s) == 0








