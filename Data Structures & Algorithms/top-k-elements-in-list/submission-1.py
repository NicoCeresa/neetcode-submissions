class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        RETURN: k most freq elements in nums
        - create counter
        - sort by freq count.sort(key=lamda x: x.values())
        - return count.keys()[:k]
        """
        count = {}
        for idx in range(len(nums)):
            if nums[idx] not in count:
                count[nums[idx]] = 1
            else:
                count[nums[idx]] += 1

        count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        return list(count.keys())[:k]
