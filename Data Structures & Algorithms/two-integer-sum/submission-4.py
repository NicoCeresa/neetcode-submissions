class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for n in range(len(nums)):
            if nums[n] in seen:
                return [seen[nums[n]], n]
            seen[target - nums[n]] = n
        return []