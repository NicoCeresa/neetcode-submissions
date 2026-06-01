class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        - return INDICES i, j
        - nums[i] + nums[j] == target
        - hashmap
        - map[target - nums[i]] = i
            [1,2,4] target: 5
            {4: 0}
            - is 5-4=1 in keys? no
            - add curr num to dict
            {4: 0,
            3: 1}
            - is 5-2=3 in keys? no. 
            - add curr num to dict
            - is 5-1=4 in keys? yes
            {4: 0,
            3: 1,
            1: 2}
            - return map[num[i]], idx
        """
        tsum = {}
        for idx in range(len(nums)):
            if nums[idx] in tsum.keys():
                return [tsum[nums[idx]], idx]
            else:
                tsum[target - nums[idx]] = idx
