class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        exact_price=0
        min_price=float("inf")
        profit=0
        max_profit=0
        for i in range(len(prices)):
            exact_price = prices[i]
            min_price = min(min_price,exact_price)
            profit = exact_price-min_price
            max_profit = max(max_profit,profit)
        return max_profit    
