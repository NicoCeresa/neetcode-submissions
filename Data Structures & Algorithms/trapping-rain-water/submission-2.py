class Solution:
    def trap(self, height: List[int]) -> int:
        # can fill water when height goes down then back up
        # have running volume sum
        # if never find
        n = len(height)
        l, r = 0, n-1
        max_l, max_r = height[l], height[r]
        tot = 0
        while l < r:
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
            if height[l] >= max_l:
                max_l = height[l]
            else:
                tot += (max_l - height[l])
            if height[r] > max_r:
                max_r = height[r]
            else:
                tot += (max_r - height[r])
        return tot
            
        