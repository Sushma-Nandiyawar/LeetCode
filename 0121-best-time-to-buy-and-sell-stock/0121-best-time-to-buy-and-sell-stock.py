class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_prof = 0

        for price in prices[1:]:
            max_prof = max(max_prof, price - min_price)
            min_price = min(min_price, price)
        return max_prof