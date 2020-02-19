#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    #solution1  40ms 93.9% 12.8MB
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(level = 0):
            if level == n:
                output.append(nums[:])
                return
            for i in range(level,n):
                nums[level] , nums[i] = nums[i] ,nums[level]
                helper(level+1)
                nums[level] , nums[i] = nums[i] , nums[level]
        
        n=len(nums)    
        output = []
        helper()
        return output

        
# @lc code=end

