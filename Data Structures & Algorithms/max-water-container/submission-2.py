class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # move left or right based on which
        max_volume = 0
        n = len(heights)
        l, r = 0, n-1
        while l < r :
            volume = (r - l) * min(heights[r], heights[l])
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            max_volume = max(max_volume, volume)            
        return max_volume 