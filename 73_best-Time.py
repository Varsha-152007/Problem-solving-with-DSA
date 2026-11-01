# Problem: Best Time to Buy and Sell Stock with Cooldown
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
# Date: 1st Nov 2026
# Time taken to solve: 35 mins

#solution
<
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        buy = -prices[0]
        sell = 0
        cooldown = 0

        for i in range(1, n):
            prev_buy = buy
            prev_sell = sell
            prev_cooldown = cooldown

            buy = max(prev_buy, prev_cooldown - prices[i])
            sell = prev_buy + prices[i]
            cooldown = max(prev_cooldown, prev_sell)

        return max(sell, cooldown)
>
