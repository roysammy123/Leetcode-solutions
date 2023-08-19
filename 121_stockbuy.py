class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=999999
        sell=0
        for i in range (0,len(prices)):
            buy=min(buy,prices[i]);
            sell=max(sell,prices[i]-buy)
        return sell
