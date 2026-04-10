class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        maxP = 0
        for price in prices:
            profit = price - min_prices
            maxP = max(maxP, profit)
            min_prices = min(min_prices, price)
        return maxP

