#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    #solution1 72ms  57%  13.4
    # def permuteUnique(self, nums: List[int]) -> List[List[int]]:


    #     def helper(level = 0):
    #         if level == n:
    #             output.append(res[:])
    #             return
    #         for i in range(n):
    #             if not used[i]:
    #                 if 0 < i  and nums[i] == nums[i-1] and not used[i-1]:
    #                     continue
    #                 used[i] = True
    #                 res.append(nums[i])
    #                 helper(level+1)
    #                 used[i] = False
    #                 res.pop()
        
    #     n=len(nums)    
    #     output = []
    #     res = []
    #     nums.sort()
    #     used = [False] * n
    #     helper()
    #     return output
    # solution2 56ms 93% 13.4MB
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        def helper(ns,pos=0):
            if len(ns) == 0:
                output.append(res[:])
                return
            for i in range(len(ns)):
                if (0 < i and ns[i]==ns[i-1] ) :
                    continue
                res.append(ns[i])
                helper(ns[:i]+ns[i+1:],i)
                res.pop()
                    
        output = []
        res = []
        nums.sort()
        # used = [False] * n
        helper(nums)
        return output

        
# @lc code=end

