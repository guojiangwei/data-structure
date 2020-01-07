#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    # solution 1
    # def climbStairs(self, n: int) -> int:
    #     res = [1] * 2
    #     res[0] = 1
    #     res[1] = 2
    #     if n == 1:
    #         return res[0]
    #     if n == 2 :
    #         return res[1]
    #     for i in range(3,n+1):
    #         res[0],res[1] = res[1],res[0]+res[1]
    #     return res[1]


# dp is the fatest function
    def climbStairs(self, n: int) -> int:
        res = [1] * (n+1)
        res[0] = 1
        res[1] = 1
        for i in range(2,n+1):
            res[i] = res[i-1]+res[i-2]
        return res[n]
        
# @lc code=end

