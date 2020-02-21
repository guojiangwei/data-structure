#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        i = end = ans = tmp_max = 0

        
        if size <= 1:
            return 0
        for i in range(size-1) :
            # tmp_max = i + 1
            tmp_max = max(tmp_max, i+nums[i])
            if i ==end:
                end = tmp_max
                ans += 1
            
        return ans
            
        
# @lc code=end

