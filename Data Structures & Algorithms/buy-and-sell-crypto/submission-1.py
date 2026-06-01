class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy low sell high 
        # if next is lower, set l to next
        # else expand window
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit