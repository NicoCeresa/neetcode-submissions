class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return: len of longest consecutive sequency that can be formed
        # option 1: sort, then use a sliding window
        # option 2: use hashmap, if n is a key +1 add to map
        d = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in d:
                length = 0
                while (i + length) in d:
                    length += 1

                longest = max(length, longest)
        return longest