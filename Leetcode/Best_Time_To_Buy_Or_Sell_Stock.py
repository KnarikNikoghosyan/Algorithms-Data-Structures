class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        j = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[j]:
                j = i
                continue
            else:
                if prices[i] - prices[j] > maxProfit:
                    maxProfit = prices[i] - prices[j]
        return maxProfit