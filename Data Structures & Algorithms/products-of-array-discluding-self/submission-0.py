class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of all except nums[i]
        # have i multiply all before and after for each i
        # very slow 
        n = len(nums)
        out = []
        for i in range(n):
            prod = 1
            if n == 0:
                for x in nums[1:]:
                    prod *= x
                out.append(prod)
            elif i == n:
                for x in nums[:-2]:
                    prod *= x
                out.append(prod)
            else:
                before = nums[:i]
                after = nums[i+1:]
                for x in before:
                    prod *= x
                for x in after:
                    prod *= x
                out.append(prod)
        return out
