class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            current_price = prices[i]

            if current_price <= min_profit:
                min_profit = current_price
            else:
                profit = current_price - min_profit

                if profit > max_profit:
                    max_profit = profit

        return max_profit
