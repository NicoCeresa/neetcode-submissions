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
            if max_l > max_r:
                r -= 1
                max_r = max(max_r, height[r])
                tot += (max_r - height[r])
            else:
                l += 1
                max_l = max(max_l, height[l])
                tot += (max_l - height[l])
        return tot
            
        