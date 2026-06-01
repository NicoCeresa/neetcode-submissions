class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix and postfix
        # prefix forward ->
        # postfix backward <- from -1 to len -1
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