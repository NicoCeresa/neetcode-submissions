class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        - group all anagrams into sublists
        - output in any order
        - we know how to find anagrams
        - naive: 
            - get count of str, loop through all sublists, 
            if find add, if nothing create new
            - sorting words
        - output list[list[str]]
        - empty, 26 long arr
        - count freq of each
        - use as key: str: list[str]
        - if not in dict create new
        - else append word
        - return dict.values()
        """
        groups = defaultdict(list)
        for wrd in strs:
            freq = [0 for _ in range(26)]
            for char in wrd:
                char_idx = ord(char.lower()) - 97
                freq[char_idx] += 1
            freq_str = tuple(freq)
            groups[freq_str].append(wrd)
        return list(groups.values())