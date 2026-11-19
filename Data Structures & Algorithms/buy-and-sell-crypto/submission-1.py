class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low=float('inf')
        ans = 0
        for i in range(len(prices)):
            low = min(prices[i],low)
            ans = max(prices[i]-low, ans)
        return ans