#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
# # solution 1
    # def moveZeroes(self, nums: List[int]) -> None:
    #     last_none_zero_posi = 0
    #     for i in range(len(nums)):
    #         if nums[i] !=0 :
    #             nums[last_none_zero_posi] = nums[i]
    #             last_none_zero_posi += 1
    #     for i in range(last_none_zero_posi,len(nums)):
    #         nums[i] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        last_none_zero_posi = 0
        for i in range(len(nums)):
            if nums[i] !=0 :
                nums[last_none_zero_posi] ,nums[i]= nums[i],nums[last_none_zero_posi]
                last_none_zero_posi += 1



        """
        Do not return anything, modify nums in-place instead.
        """
        
# @lc code=end

