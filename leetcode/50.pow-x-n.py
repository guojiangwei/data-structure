#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    # solution time limit exceeded
    # def myPow(self, x: float, n: int) -> float:
    #     ans = float(1)
    #     if n < 0:
    #         n = -n
    #         x = 1/x
    #     while n >0 :
    #         ans = ans*x
    #         n -= 1
    #     return  ans
    # solution2 44ms 38.33% 13MB
    def myPow(self, x: float, n: int) -> float:
        ans = float(1)
        if n < 0:
            n = -n
            x = 1/x
        tmp = x
    
        while n >0 :
            if n%2 == 1:
                ans = tmp*ans
            tmp = tmp * tmp
            n = int(n/2)
        return  ans


        
# @lc code=end

