class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cheapest = prices[0]
        profit = 0
        max_profit = 0
        for right in range(1,len(prices)):
            cheapest = min(cheapest, prices[right])

            profit = max(0,prices[right] - cheapest)

            max_profit = max(max_profit, profit)

        return max_profit

        
