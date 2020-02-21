#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    # solution1 172ms 6.6% 5% 29.7MB
    # def maxProfit(self, prices: List[int]) -> int:
    #     size = len(prices)
    #     total = 0
    #     for i in range(size-1):
    #         if prices[i] < prices[i+1]:
    #             total +=   prices[i+1]-prices[i]
    #     return total

# solution as fast as obove
    # def maxProfit(self, prices: List[int]) -> int:
    #     total = 0
    #     for i in range(1, len(prices)):
    #         if prices[i] -  prices[i-1] >0:
    #             total += (prices[i] - prices[i - 1])
    #     return total
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0:
            return 0
        tmp = prices[0]
        sum = 0
        for i in range(1, size):
            if prices[i] > tmp:
                sum += prices[i] - tmp
            tmp = prices[i]
        return sum
# @lc code=end

