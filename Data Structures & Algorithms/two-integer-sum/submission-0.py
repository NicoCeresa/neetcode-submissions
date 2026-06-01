class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dict st target - num in dict and dict[diff] == idx
        seen = dict()
        for idx, n in enumerate(nums):
            diff = target - n
            if n in seen:
                return [seen[n], idx]

            else:
                seen[diff] = idx
        return False 