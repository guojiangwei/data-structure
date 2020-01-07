#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        diff_at = 0
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                nums[diff_at]=nums[i]
                continue
            diff_at +=1
            nums[diff_at]=nums[i]

        return diff_at+1
        
# @lc code=end

