class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of all except nums[i]
        # have i multiply all before and after for each i
        # very slow 
        out = [1] * len(nums)
        pre_prod = 1
        for i in range(len(nums)):
            out[i] = pre_prod
            pre_prod *= nums[i]
        print(out)

        post_prod = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= post_prod
            post_prod *= nums[i]

        return out